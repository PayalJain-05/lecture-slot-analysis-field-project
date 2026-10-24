import pandas as pd
from pathlib import Path


# ==================================================
# DATA FOLDER
# ==================================================

data_folder = Path("data")


# ==================================================
# LOAD DATASETS
# ==================================================

student_survey = pd.read_excel(
    data_folder / "cleaned_student_survey.xlsx"
)

classroom_observation = pd.read_excel(
    data_folder / "cleaned_classroom_observation.xlsx"
)

classroom_master = pd.read_csv(
    data_folder / "cleaned_classroom_master_data.csv"
)

timetable_file = data_folder / "cleaned_timetable_data.xlsx"


# ==================================================
# CHECK DATA
# ==================================================

print("=" * 70)
print("RECOMMENDATION ENGINE - DATA LOADING")
print("=" * 70)

print("\nStudent Survey:")
print(student_survey.shape)

print("\nClassroom Observation:")
print(classroom_observation.shape)

print("\nClassroom Master:")
print(classroom_master.shape)

print("\nTimetable Sheets:")

excel_file = pd.ExcelFile(timetable_file)

print(excel_file.sheet_names)

print("\n" + "=" * 70)
print("ALL DATASETS LOADED SUCCESSFULLY")
print("=" * 70)


# ==================================================
# LOAD STRUCTURED TIMETABLE
# ==================================================

timetable_data = []

timetable_sheets = [
    sheet
    for sheet in excel_file.sheet_names
    if sheet != "Combined_Data"
]


for sheet in timetable_sheets:

    timetable = pd.read_excel(
        timetable_file,
        sheet_name=sheet,
        header=None
    )

    # --------------------------------------------------
    # FIND RECOMMENDATION-SYSTEM HEADER
    # --------------------------------------------------

    header_row = None

    for i in range(len(timetable)):

        row_values = (
            timetable.iloc[i]
            .astype(str)
            .tolist()
        )

        if (
            "Day" in row_values
            and "Time_Slot" in row_values
            and "Subject" in row_values
            and "Division" in row_values
            and "Classroom" in row_values
            and "Session_Type" in row_values
        ):

            header_row = i
            break


    if header_row is None:

        print(
            f"\nWARNING: Could not find timetable data in {sheet}"
        )

        continue


    # --------------------------------------------------
    # TAKE ROWS AFTER HEADER
    # --------------------------------------------------

    timetable_clean = (
        timetable
        .iloc[header_row + 1:]
        .copy()
    )


    # Keep only required columns

    timetable_clean = (
        timetable_clean
        .iloc[:, :6]
    )


    timetable_clean.columns = [
        "Day",
        "Time_Slot",
        "Subject",
        "Division",
        "Classroom",
        "Session_Type"
    ]


    # Remove completely empty rows

    timetable_clean = (
        timetable_clean
        .dropna(how="all")
    )


    timetable_data.append(
        timetable_clean
    )


# --------------------------------------------------
# COMBINE ALL DIVISIONS
# --------------------------------------------------

timetable_df = pd.concat(
    timetable_data,
    ignore_index=True
)


# ==================================================
# CLEAN TIMETABLE VALUES
# ==================================================

for column in [
    "Day",
    "Time_Slot",
    "Subject",
    "Division",
    "Classroom",
    "Session_Type"
]:

    timetable_df[column] = (
        timetable_df[column]
        .astype(str)
        .str.strip()
    )


# ==================================================
# TIMETABLE CHECK
# ==================================================

print("\n" + "=" * 70)
print("STRUCTURED TIMETABLE CHECK")
print("=" * 70)

print("\nTotal timetable rows:")
print(len(timetable_df))

print("\nDivisions:")
print(timetable_df["Division"].unique())

print("\nDays:")
print(timetable_df["Day"].unique())

print("\nSession Types:")
print(
    timetable_df["Session_Type"]
    .value_counts()
)

print("\nFirst 20 rows:")

print(
    timetable_df
    .head(20)
    .to_string(index=False)
)

print("\n" + "=" * 70)
print("TIMETABLE STRUCTURED SUCCESSFULLY")
print("=" * 70)


# ==================================================
# ATTENDANCE SCORE FUNCTION
# ==================================================

def calculate_attendance_score(
    attendance_percentage
):

    if attendance_percentage >= 85:
        return 40

    elif attendance_percentage >= 75:
        return 32

    elif attendance_percentage >= 65:
        return 24

    elif attendance_percentage >= 50:
        return 16

    else:
        return 8


# ==================================================
# TEST ATTENDANCE SCORE
# ==================================================

print("\n" + "=" * 70)
print("ATTENDANCE SCORE TEST")
print("=" * 70)

test_values = [
    90,
    80,
    70,
    55,
    40
]

for attendance in test_values:

    score = calculate_attendance_score(
        attendance
    )

    print(
        f"Attendance: {attendance}% "
        f"→ Score: {score}/40"
    )


# ==================================================
# STUDENT TIMING PREFERENCE CHECK
# ==================================================

preference_column = (
    "Which lecture timing do you find most comfortable?"
)


preference_counts = (
    student_survey[
        preference_column
    ]
    .value_counts()
)


print("\n" + "=" * 70)
print("STUDENT TIMING PREFERENCE CHECK")
print("=" * 70)

print("\nComfortable Timing Counts:")

print(preference_counts)

print("\nMost preferred timing:")

most_preferred_timing = (
    preference_counts
    .idxmax()
)

maximum_preference_count = (
    preference_counts
    .max()
)

print(
    f"Timing : {most_preferred_timing}"
)

print(
    f"Responses : {maximum_preference_count}"
)


# ==================================================
# STUDENT TIMING PREFERENCE SCORE
# ==================================================

maximum_preference_count = (
    preference_counts
    .max()
)


def calculate_preference_score(
    response_count
):

    score = (
        response_count
        / maximum_preference_count
    ) * 25

    return round(
        score,
        2
    )


print("\nPreference Scores:")

for timing, count in preference_counts.items():

    score = calculate_preference_score(
        count
    )

    print(
        f"{timing}: "
        f"{count} responses "
        f"→ {score}/25"
    )


# ==================================================
# CONCENTRATION IMPACT CHECK
# ==================================================

concentration_column = (
    "Does the timing of a lecture affect your concentration?"
)


concentration_counts = (
    student_survey[
        concentration_column
    ]
    .value_counts()
)


print("\n" + "=" * 70)
print("CONCENTRATION IMPACT CHECK")
print("=" * 70)

print("\nConcentration Impact Counts:")

print(concentration_counts)

print("\nTotal Responses:")

print(
    concentration_counts.sum()
)


# ==================================================
# CONCENTRATION IMPACT SCORE
# ==================================================

impact_values = {
    "Never": 0,
    "Rarely": 25,
    "Sometimes": 50,
    "Often": 75,
    "Very Often": 100
}


weighted_impact = 0


for response, count in (
    concentration_counts.items()
):

    impact = impact_values[
        response
    ]

    weighted_impact += (
        impact * count
    )


average_impact = (
    weighted_impact
    / concentration_counts.sum()
)


concentration_score = (
    1 - (
        average_impact
        / 100
    )
) * 15


concentration_score = round(
    concentration_score,
    2
)


print("\nConcentration Score:")

print(
    f"{concentration_score}/15"
)

print(
    f"Average Impact: "
    f"{average_impact:.2f}/100"
)


# ==================================================
# SCHEDULE CONDITIONS CHECK
# ==================================================

continuous_column = (
    "How often do you have 3 or more lectures continuously?"
)

gaps_column = (
    "How often do you have long gaps between lectures?"
)


continuous_counts = (
    student_survey[
        continuous_column
    ]
    .value_counts()
)

gaps_counts = (
    student_survey[
        gaps_column
    ]
    .value_counts()
)


print("\n" + "=" * 70)
print("SCHEDULE CONDITIONS CHECK")
print("=" * 70)

print("\n3 or More Continuous Lectures:")

print(continuous_counts)

print("\nTotal Responses:")

print(
    continuous_counts.sum()
)

print("\nLong Gaps Between Lectures:")

print(gaps_counts)

print("\nTotal Responses:")

print(
    gaps_counts.sum()
)


# ==================================================
# SCHEDULE CONDITIONS SCORE
# ==================================================

schedule_frequency_values = {
    "Never": 0,
    "Occasionally": 25,
    "Sometimes": 50,
    "Often": 75,
    "Always": 100
}


def calculate_schedule_burden(
    counts
):

    weighted_burden = 0


    for response, count in counts.items():

        burden = (
            schedule_frequency_values[
                response
            ]
        )

        weighted_burden += (
            burden * count
        )


    average_burden = (
        weighted_burden
        / counts.sum()
    )


    return average_burden


continuous_burden = (
    calculate_schedule_burden(
        continuous_counts
    )
)

gaps_burden = (
    calculate_schedule_burden(
        gaps_counts
    )
)


continuous_score = (
    1 - (
        continuous_burden
        / 100
    )
) * 5


gaps_score = (
    1 - (
        gaps_burden
        / 100
    )
) * 5


continuous_score = round(
    continuous_score,
    2
)

gaps_score = round(
    gaps_score,
    2
)


schedule_score = round(
    continuous_score
    + gaps_score,
    2
)


print("\nSchedule Scores:")

print(
    f"Continuous Lecture Score: "
    f"{continuous_score}/5"
)

print(
    f"Long Gap Score: "
    f"{gaps_score}/5"
)

print(
    f"Total Schedule Score: "
    f"{schedule_score}/10"
)


# ==================================================
# ON-TIME PERFORMANCE CHECK
# ==================================================

start_time_column = (
    "Started_On_Time"
)

end_time_column = (
    "Ended_On_Time"
)


start_time_counts = (
    classroom_observation[
        start_time_column
    ]
    .value_counts(
        dropna=False
    )
)

end_time_counts = (
    classroom_observation[
        end_time_column
    ]
    .value_counts(
        dropna=False
    )
)


print("\n" + "=" * 70)
print("ON-TIME PERFORMANCE CHECK")
print("=" * 70)

print("\nStarted On Time:")

print(start_time_counts)

print("\nEnded On Time:")

print(end_time_counts)


# ==================================================
# ON-TIME PERFORMANCE SCORE
# ==================================================

valid_start = (
    classroom_observation[
        start_time_column
    ]
    .dropna()
)

valid_end = (
    classroom_observation[
        end_time_column
    ]
    .dropna()
)


start_on_time_rate = (
    (
        valid_start == "Yes"
    ).sum()
    / len(valid_start)
) * 100


end_on_time_rate = (
    (
        valid_end == "Yes"
    ).sum()
    / len(valid_end)
) * 100


start_score = (
    start_on_time_rate
    / 100
) * 5


end_score = (
    end_on_time_rate
    / 100
) * 5


start_score = round(
    start_score,
    2
)

end_score = round(
    end_score,
    2
)


on_time_score = round(
    start_score
    + end_score,
    2
)


print("\nOn-Time Performance Score:")

print(
    f"Start On-Time Rate: "
    f"{start_on_time_rate:.2f}% "
    f"→ {start_score}/5"
)

print(
    f"End On-Time Rate: "
    f"{end_on_time_rate:.2f}% "
    f"→ {end_score}/5"
)

print(
    f"Total On-Time Score: "
    f"{on_time_score}/10"
)


# ==================================================
# ATTENDANCE SCORE FOR EACH TIME SLOT
# ==================================================

slot_attendance = (
    classroom_observation
    .groupby("Time_Slot")[
        "Attendance_Percentage"
    ]
    .mean()
    .dropna()
)


slot_attendance_scores = {}


for (
    time_slot,
    average_attendance
) in slot_attendance.items():

    score = calculate_attendance_score(
        average_attendance
    )

    slot_attendance_scores[
        time_slot
    ] = score


print("\n" + "=" * 70)
print("ATTENDANCE SCORE BY TIME SLOT")
print("=" * 70)


for (
    time_slot,
    average_attendance
) in slot_attendance.items():

    score = (
        slot_attendance_scores[
            time_slot
        ]
    )

    print(
        f"{time_slot}: "
        f"Average Attendance = "
        f"{average_attendance:.2f}% "
        f"→ Score = {score}/40"
    )


# ==================================================
# PREFERENCE SCORE FOR EACH TIME SLOT
# ==================================================

preference_scores = {}


for timing, count in (
    preference_counts.items()
):

    score = (
        calculate_preference_score(
            count
        )
    )

    preference_scores[
        timing
    ] = score


print("\n" + "=" * 70)
print("STUDENT PREFERENCE SCORE BY TIME SLOT")
print("=" * 70)


for timing, score in (
    preference_scores.items()
):

    print(
        f"{timing}: "
        f"Preference Score = {score}/25"
    )


# ==================================================
# STORE GLOBAL SCORES
# ==================================================

global_concentration_score = (
    concentration_score
)

global_schedule_score = (
    schedule_score
)

global_on_time_score = (
    on_time_score
)


print("\n" + "=" * 70)
print("GLOBAL SCORES")
print("=" * 70)

print(
    f"Concentration Score: "
    f"{global_concentration_score}/15"
)

print(
    f"Schedule Conditions Score: "
    f"{global_schedule_score}/10"
)

print(
    f"On-Time Performance Score: "
    f"{global_on_time_score}/10"
)


# ==================================================
# LECTURE SLOT EFFICIENCY SCORE SETUP
# ==================================================

print("\n" + "=" * 70)
print("LECTURE SLOT EFFICIENCY SCORE SETUP")
print("=" * 70)

print("\nScoring Components:")

print(
    "Attendance Performance : 40 points"
)

print(
    "Student Timing Preference : 25 points"
)

print(
    "Concentration Impact : 15 points"
)

print(
    "Schedule Conditions : 10 points"
)

print(
    "On-Time Performance : 10 points"
)

print("\nMaximum Total Score: 100")


# ==================================================
# CALCULATE BASE SLOT EFFICIENCY SCORES
# ==================================================

slot_scores = []


for (
    time_slot,
    attendance_score
) in slot_attendance_scores.items():

    preference_score = (
        preference_scores.get(
            time_slot,
            None
        )
    )


    if preference_score is not None:

        total_score = (
            attendance_score
            + preference_score
            + global_concentration_score
            + global_schedule_score
            + global_on_time_score
        )

        total_score = round(
            total_score,
            2
        )

    else:

        total_score = None


    slot_scores.append({

        "Time_Slot": time_slot,

        "Attendance_Score":
            attendance_score,

        "Preference_Score":
            preference_score,

        "Concentration_Score":
            global_concentration_score,

        "Schedule_Score":
            global_schedule_score,

        "On_Time_Score":
            global_on_time_score,

        "Total_Score":
            total_score
    })


slot_score_df = pd.DataFrame(
    slot_scores
)


print("\n" + "=" * 70)
print("BASE LECTURE SLOT EFFICIENCY SCORES")
print("=" * 70)

print(
    slot_score_df
    .to_string(index=False)
)


# ==================================================
# CHECK TIME SLOT FORMATS
# ==================================================

print("\n" + "=" * 70)
print("TIME SLOT FORMAT CHECK")
print("=" * 70)

print("\nObservation Time Slots:")

for slot in sorted(
    classroom_observation[
        "Time_Slot"
    ]
    .dropna()
    .unique()
):

    print(slot)


print("\nSurvey Timing Values:")

for timing in sorted(
    student_survey[
        preference_column
    ]
    .dropna()
    .unique()
):

    print(timing)


print("\nTimetable Time Slots:")

for slot in sorted(
    timetable_df[
        "Time_Slot"
    ]
    .dropna()
    .unique()
):

    print(slot)


# ==================================================
# PROBLEM DETECTION
# ==================================================

print("\n" + "=" * 70)
print("PROBLEM DETECTION - LOW SCORING TIME SLOTS")
print("=" * 70)


problem_slots = (
    slot_score_df[
        slot_score_df[
            "Total_Score"
        ].notna()
    ]
    .copy()
)


problem_slots = (
    problem_slots[
        problem_slots[
            "Total_Score"
        ] < 60
    ]
)


print("\nTime slots needing review:")


if problem_slots.empty:

    print(
        "No low-scoring time slots found."
    )

else:

    print(
        problem_slots[
            [
                "Time_Slot",
                "Attendance_Score",
                "Preference_Score",
                "Concentration_Score",
                "Schedule_Score",
                "On_Time_Score",
                "Total_Score"
            ]
        ]
        .to_string(index=False)
    )


# ==================================================
# SHOW LECTURES IN PROBLEM TIME SLOTS
# ==================================================

print("\n" + "=" * 70)
print("LECTURES IN PROBLEM TIME SLOTS")
print("=" * 70)


problem_slot_names = (
    problem_slots[
        "Time_Slot"
    ]
    .tolist()
)


problem_lectures = (
    timetable_df[
        timetable_df[
            "Time_Slot"
        ].isin(problem_slot_names)
    ]
    .copy()
)


print(
    problem_lectures[
        [
            "Day",
            "Time_Slot",
            "Subject",
            "Division",
            "Classroom",
            "Session_Type"
        ]
    ]
    .to_string(index=False)
)


# ==================================================
# KEEP ONLY ACTUAL LECTURES
# ==================================================

problem_lectures = (
    timetable_df[
        timetable_df[
            "Time_Slot"
        ].isin(problem_slot_names)

        & (
            timetable_df[
                "Session_Type"
            ] == "Lecture"
        )

        & (
            timetable_df[
                "Subject"
            ] != "FREE"
        )
    ]
    .copy()
)


print("\n" + "=" * 70)
print("ACTUAL LECTURES IN PROBLEM TIME SLOTS")
print("=" * 70)


print(
    problem_lectures[
        [
            "Day",
            "Time_Slot",
            "Subject",
            "Division",
            "Classroom",
            "Session_Type"
        ]
    ]
    .to_string(index=False)
)


# ==================================================
# ALL VALID TIME SLOTS
# ==================================================

all_time_slots = [

    "1:00-1:40",

    "1:40-2:20",

    "2:20-3:00",

    "3:30-4:10",

    "4:10-4:50",

    "4:50-5:30",

    "5:30-6:10",

    "6:10-6:50"
]


# ==================================================
# FIND ALL BETTER AVAILABLE ALTERNATIVE SLOTS
# ==================================================

print("\n" + "=" * 70)
print("FINDING ALL BETTER AVAILABLE ALTERNATIVE SLOTS")
print("=" * 70)


alternative_slots = []


for _, lecture in (
    problem_lectures.iterrows()
):

    division = lecture[
        "Division"
    ]

    day = lecture[
        "Day"
    ]

    current_slot = lecture[
        "Time_Slot"
    ]


    # --------------------------------------------------
    # CURRENT SCORE
    # --------------------------------------------------

    current_score_row = (
        slot_score_df[
            slot_score_df[
                "Time_Slot"
            ] == current_slot
        ]
    )


    if current_score_row.empty:
        continue


    current_score = (
        current_score_row.iloc[0][
            "Total_Score"
        ]
    )


    if pd.isna(current_score):
        continue


    # --------------------------------------------------
    # SLOTS ALREADY USED BY THIS DIVISION
    # ON THIS DAY
    # --------------------------------------------------

    used_slots_for_division = (
        timetable_df[
            (
                timetable_df[
                    "Division"
                ] == division
            )

            & (
                timetable_df[
                    "Day"
                ] == day
            )

            & (
                timetable_df[
                    "Session_Type"
                ] == "Lecture"
            )
        ][
            "Time_Slot"
        ]
        .tolist()
    )


    # --------------------------------------------------
    # CHECK EVERY POSSIBLE SLOT
    # --------------------------------------------------

    for alternative_slot in (
        all_time_slots
    ):


        # Current slot cannot be an alternative

        if (
            alternative_slot
            == current_slot
        ):

            continue


        # Division already has a lecture there

        if (
            alternative_slot
            in used_slots_for_division
        ):

            continue


        # Unknown score cannot be used

        score_row = (
            slot_score_df[
                slot_score_df[
                    "Time_Slot"
                ] == alternative_slot
            ]
        )


        if score_row.empty:
            continue


        alternative_score = (
            score_row.iloc[0][
                "Total_Score"
            ]
        )


        if pd.isna(
            alternative_score
        ):

            continue


        # Alternative MUST be better

        if (
            alternative_score
            <= current_score
        ):

            continue


        # --------------------------------------------------
        # SAVE EVERY BETTER ALTERNATIVE
        # --------------------------------------------------

        alternative_slots.append({

            "Day":
                day,

            "Division":
                division,

            "Subject":
                lecture[
                    "Subject"
                ],

            "Classroom":
                lecture[
                    "Classroom"
                ],

            "Current_Slot":
                current_slot,

            "Current_Score":
                round(
                    current_score,
                    2
                ),

            "Alternative_Slot":
                alternative_slot,

            "Alternative_Score":
                round(
                    alternative_score,
                    2
                ),

            "Score_Improvement":
                round(
                    alternative_score
                    - current_score,
                    2
                )
        })


alternative_slots_df = (
    pd.DataFrame(
        alternative_slots
    )
)


print("\n" + "=" * 70)
print("ALL BETTER AVAILABLE ALTERNATIVE SLOTS")
print("=" * 70)


if alternative_slots_df.empty:

    print(
        "No better available alternative slots found."
    )

else:

    alternative_slots_df = (
        alternative_slots_df
        .sort_values(
            [
                "Day",
                "Division",
                "Subject",
                "Current_Slot",
                "Alternative_Score"
            ],
            ascending=[
                True,
                True,
                True,
                True,
                False
            ]
        )
        .reset_index(drop=True)
    )


    print(
        alternative_slots_df
        .to_string(index=False)
    )


# ==================================================
# BEST ALTERNATIVE OPTIONS
# ==================================================

print("\n" + "=" * 70)
print("BEST ALTERNATIVE OPTIONS")
print("=" * 70)


if alternative_slots_df.empty:

    best_alternatives_df = (
        pd.DataFrame()
    )

    print(
        "No alternative options found."
    )

else:

    # IMPORTANT:
    # Do NOT remove duplicate subjects here.
    #
    # A subject can occur more than once
    # for the same division/day at different
    # current slots.
    #
    # Therefore lecture identity is:
    #
    # Day + Division + Subject + Current_Slot

    best_alternatives_df = (
        alternative_slots_df
        .sort_values(
            [
                "Day",
                "Division",
                "Subject",
                "Current_Slot",
                "Alternative_Score"
            ],
            ascending=[
                True,
                True,
                True,
                True,
                False
            ]
        )
        .reset_index(drop=True)
    )


    print(
        best_alternatives_df
        .to_string(index=False)
    )


# ==================================================
# CLASSROOM-LEVEL OBSERVED UTILIZATION
# ==================================================

print("\n" + "=" * 70)
print("CLASSROOM-LEVEL OBSERVED UTILIZATION")
print("=" * 70)


classroom_utilization = (
    classroom_observation
    .groupby("Classroom")
    .agg(
        Average_Students=(
            "Students_Present",
            "mean"
        ),

        Observations=(
            "Students_Present",
            "count"
        )
    )
    .reset_index()
)


classroom_utilization = (
    classroom_utilization
    .merge(
        classroom_master[
            [
                "Classroom",
                "Capacity"
            ]
        ],

        on="Classroom",

        how="left"
    )
)


classroom_utilization[
    "Utilization_Percentage"
] = (

    classroom_utilization[
        "Average_Students"
    ]

    /

    classroom_utilization[
        "Capacity"
    ]

    * 100
)


classroom_utilization[
    "Utilization_Percentage"
] = (
    classroom_utilization[
        "Utilization_Percentage"
    ]
    .round(2)
)


print(
    classroom_utilization
    .to_string(index=False)
)


# ==================================================
# ESTIMATE STUDENT COUNT BY DIVISION
# ==================================================

print("\n" + "=" * 70)
print("ESTIMATED STUDENT COUNT BY DIVISION")
print("=" * 70)


division_student_estimates = (
    classroom_observation
    .groupby("Division")[
        "Students_Present"
    ]
    .mean()
    .dropna()
    .round(2)
)


print(
    division_student_estimates
)


# ==================================================
# GENERATE CONFLICT-FREE RECOMMENDATIONS
# ==================================================

print("\n" + "=" * 70)
print("CONFLICT-FREE RECOMMENDATIONS")
print("=" * 70)


conflict_free_recommendations = []


if alternative_slots_df.empty:

    conflict_free_df = (
        pd.DataFrame()
    )

else:

    # --------------------------------------------------
    # USED TIME SLOTS
    #
    # Prevent two recommended lectures from the
    # same division/day being moved into the same slot.
    # --------------------------------------------------

    used_recommended_slots = {}


    # --------------------------------------------------
    # RESERVED CLASSROOMS
    #
    # Prevent two recommendations from using
    # the same classroom at the same day/slot.
    # --------------------------------------------------

    reserved_classrooms = {}


    # --------------------------------------------------
    # PROCESS LECTURES
    #
    # Higher improvement gets considered first.
    #
    # IMPORTANT:
    # Grouping includes Current_Slot so that
    # duplicate subjects at different times remain
    # separate lectures.
    # --------------------------------------------------

    candidate_lectures = (
        alternative_slots_df
        .sort_values(
            [
                "Day",
                "Division",
                "Subject",
                "Current_Slot",
                "Alternative_Score"
            ],
            ascending=[
                True,
                True,
                True,
                True,
                False
            ]
        )
    )


    for (
        day,
        division,
        subject,
        current_slot
    ), lecture_candidates in (
        candidate_lectures
        .groupby(
            [
                "Day",
                "Division",
                "Subject",
                "Current_Slot"
            ]
        )
    ):


        # --------------------------------------------------
        # BASIC LECTURE INFORMATION
        # --------------------------------------------------

        first_candidate = (
            lecture_candidates
            .iloc[0]
        )


        current_classroom = (
            first_candidate[
                "Classroom"
            ]
        )


        current_score = (
            first_candidate[
                "Current_Score"
            ]
        )


        division_day_key = (
            day,
            division
        )


        # --------------------------------------------------
        # CREATE SLOT TRACKER
        # --------------------------------------------------

        if (
            division_day_key
            not in used_recommended_slots
        ):

            used_recommended_slots[
                division_day_key
            ] = set()


        recommendation_found = False


        # --------------------------------------------------
        # TRY BEST ALTERNATIVE FIRST
        # --------------------------------------------------

        lecture_candidates = (
            lecture_candidates
            .sort_values(
                "Alternative_Score",
                ascending=False
            )
        )


        for _, candidate in (
            lecture_candidates.iterrows()
        ):


            alternative_slot = (
                candidate[
                    "Alternative_Slot"
                ]
            )


            alternative_score = (
                candidate[
                    "Alternative_Score"
                ]
            )


            # --------------------------------------------------
            # CHECK DIVISION CONFLICT
            # --------------------------------------------------

            if (
                alternative_slot
                in used_recommended_slots[
                    division_day_key
                ]
            ):

                continue


            # --------------------------------------------------
            # FIND CLASSROOMS ALREADY OCCUPIED
            # IN THE ORIGINAL TIMETABLE
            # --------------------------------------------------

            occupied_rooms = (
                timetable_df[
                    (
                        timetable_df[
                            "Day"
                        ] == day
                    )

                    & (
                        timetable_df[
                            "Time_Slot"
                        ]
                        == alternative_slot
                    )

                    & (
                        timetable_df[
                            "Session_Type"
                        ]
                        == "Lecture"
                    )
                ][
                    "Classroom"
                ]
                .dropna()
                .unique()
                .tolist()
            )


            # --------------------------------------------------
            # FIND CLASSROOMS ALREADY RESERVED
            # BY AN EARLIER RECOMMENDATION
            # --------------------------------------------------

            classroom_key = (
                day,
                alternative_slot
            )


            if (
                classroom_key
                not in reserved_classrooms
            ):

                reserved_classrooms[
                    classroom_key
                ] = set()


            occupied_rooms.extend(
                list(
                    reserved_classrooms[
                        classroom_key
                    ]
                )
            )


            occupied_rooms = list(
                set(
                    occupied_rooms
                )
            )


            # --------------------------------------------------
            # FIND ACTUALLY AVAILABLE CLASSROOMS
            # --------------------------------------------------

            available_rooms = (
                classroom_master[
                    ~classroom_master[
                        "Classroom"
                    ].isin(
                        occupied_rooms
                    )
                ]
                .copy()
            )


            if available_rooms.empty:

                continue


            # --------------------------------------------------
            # ESTIMATE STUDENT COUNT
            # --------------------------------------------------

            estimated_students = (
                division_student_estimates
                .get(
                    division,
                    None
                )
            )


            if estimated_students is None:

                continue


            # --------------------------------------------------
            # CLASSROOM CAPACITY CHECK
            # --------------------------------------------------

            suitable_rooms = (
                available_rooms[
                    available_rooms[
                        "Capacity"
                    ] >= estimated_students
                ]
                .copy()
            )


            if suitable_rooms.empty:

                continue


            # --------------------------------------------------
            # PREFER CURRENT CLASSROOM
            # IF IT IS FREE AND SUITABLE
            # --------------------------------------------------

            suitable_room_names = (
                suitable_rooms[
                    "Classroom"
                ]
                .tolist()
            )


            if (
                current_classroom
                in suitable_room_names
            ):

                recommended_classroom = (
                    current_classroom
                )

            else:

                recommended_classroom = (
                    suitable_room_names[0]
                )


            # --------------------------------------------------
            # FINAL ACCEPTANCE
            # --------------------------------------------------

            used_recommended_slots[
                division_day_key
            ].add(
                alternative_slot
            )


            reserved_classrooms[
                classroom_key
            ].add(
                recommended_classroom
            )


            conflict_free_recommendations.append({

                "Day":
                    day,

                "Division":
                    division,

                "Subject":
                    subject,

                "Current_Slot":
                    current_slot,

                "Recommended_Slot":
                    alternative_slot,

                "Current_Classroom":
                    current_classroom,

                "Recommended_Classroom":
                    recommended_classroom,

                "Current_Score":
                    current_score,

                "Recommended_Score":
                    alternative_score,

                "Score_Improvement":
                    round(
                        alternative_score
                        - current_score,
                        2
                    )
            })


            recommendation_found = True

            break


        # --------------------------------------------------
        # IF NO ALTERNATIVE WORKS:
        # DO NOT FORCE A RECOMMENDATION
        # --------------------------------------------------

        if not recommendation_found:

            continue


    # --------------------------------------------------
    # FINAL DATAFRAME
    # --------------------------------------------------

    conflict_free_df = (
        pd.DataFrame(
            conflict_free_recommendations
        )
    )


# ==================================================
# FINAL OUTPUT
# ==================================================

if conflict_free_df.empty:

    print(
        "No conflict-free recommendations found."
    )

else:

    conflict_free_df = (
        conflict_free_df
        .sort_values(
            [
                "Day",
                "Division",
                "Recommended_Slot"
            ]
        )
        .reset_index(drop=True)
    )


    print(
        conflict_free_df
        .to_string(index=False)
    )


# ==================================================
# RECOMMENDATION SUMMARY
# ==================================================

print("\n" + "=" * 70)
print("RECOMMENDATION SUMMARY")
print("=" * 70)


print(
    f"\nTotal problem lectures checked: "
    f"{len(problem_lectures)}"
)


print(
    f"Total better alternative options found: "
    f"{len(alternative_slots_df)}"
)


print(
    f"Total conflict-free recommendations: "
    f"{len(conflict_free_df)}"
)


if not conflict_free_df.empty:

    print(
        "\nThe system recommends only changes that:"
    )

    print(
        "1. Move the lecture to a higher-scoring slot."
    )

    print(
        "2. Keep the division free at the new slot."
    )

    print(
        "3. Have a suitable available classroom."
    )

    print(
        "4. Do not create a classroom conflict."
    )

    print(
        "5. Prefer the existing classroom when possible."
    )

    print(
        "6. Do not force a recommendation when no valid "
        "alternative exists."
    )

else:

    print(
        "\nNo valid conflict-free timetable changes "
        "were found."
    )


print("\n" + "=" * 70)
print("RECOMMENDATION ENGINE COMPLETED")
print("=" * 70)