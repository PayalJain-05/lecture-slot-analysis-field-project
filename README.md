# lecture-slot-analysis-field-project
A data-driven college project focused on analyzing classroom utilization, lecture schedules, and student feedback. Developed a Power BI dashboard to identify scheduling inefficiencies and a prototyp# Smart Lecture Slot Utilization and Classroom Efficiency Analysis

A college field project focused on understanding lecture timings, classroom utilization, and student experiences to identify scheduling issues and explore practical improvements using data analysis.

## 1. About the Project

A college timetable determines when lectures take place, which classrooms are assigned, and how available academic spaces are used throughout the day. However, a timetable does not always guarantee that lecture slots and classrooms are being used effectively.

Some lecture timings may be less comfortable for students, certain classrooms may become overcrowded, and other rooms may not be used to their full capacity. Students may also experience tiredness and classroom temperature concerns that affect their daily college experience.

This project uses student survey responses, classroom observations, and college timetable information to study these issues. The collected data was organized and analyzed to identify patterns in lecture timing preferences, classroom conditions, and slot efficiency.

An interactive **Power BI dashboard** was developed to present the findings visually. A recommendation prototype called **SlotSense** was also created to explore possible improvements to lecture timings and classroom allocation.

The aim is to support more informed scheduling decisions while considering classroom capacity, timetable conflicts, and student preferences.

## 2. Project Objectives

- **Lecture Slot Analysis:** Compare lecture timings using the efficiency scores calculated in the project and examine student timing preferences.
- **Classroom Utilization Analysis:** Study classroom observations to identify conditions marked as optimal or overcrowded.
- **Student Feedback Analysis:** Understand students' preferred lecture timings and reported concerns, including tiredness and classroom temperature.
- **Dashboard Development:** Present the collected data and analysis through an interactive Power BI dashboard.
- **Recommendation Prototype:** Develop SlotSense to suggest possible alternative lecture timings while checking classroom capacity and timetable conflicts.

## 3. Data Collection

The project used multiple data sources to understand the problem from both a scheduling perspective and a student-experience perspective.

| Data Source | Details |
|---|---|
| Student survey | 200 responses collected through a Google Form containing 36 questions |
| Classroom observations | 120 observations used to study classroom conditions and occupancy |
| College timetable | Information about lecture timings, subjects, divisions, and classroom assignments |
| Student feedback | Responses about preferred lecture timings, tiredness, and classroom temperature concerns |

Combining these sources helped us examine the existing timetable alongside classroom observations and student feedback.

## 4. Data Cleaning and Preparation

Before analysis, the collected information was organized into structured tables using Microsoft Excel.

The preparation process involved:

1. Organizing the collected records into structured tables.
2. Reviewing the data for missing or incomplete entries.
3. Keeping related information in a consistent format.
4. Preparing the data for comparison and analysis.
5. Making the information suitable for the Power BI dashboard and SlotSense prototype.

This preparation helped make the data easier to analyze and compare across different lecture timings and classroom conditions.

## 5. Data Analysis

The prepared data was examined across three main areas.

### Lecture Timing Performance

Efficiency scores were compared to identify relatively stronger lecture slots and timings that required further review.

### Classroom Conditions

The classroom observations were analyzed to understand how frequently different conditions were recorded, including observations marked as optimal or overcrowded.

### Student Preferences and Concerns

Survey responses were examined to identify preferred lecture timings and reported concerns such as tiredness and air-conditioning or room-temperature issues.

The analysis combined these findings to provide a broader understanding of the relationship between scheduling, classroom usage, and student experience.

## 6. Key Findings

### Classroom Observations

Out of 120 classroom observations:

| Observation Category | Number of Observations |
|---|---:|
| Marked as optimal | 76 |
| Marked as overcrowded | 26 |
| Other observations | 18 |
| **Total** | **120** |

These results show that although many observations were marked as optimal, overcrowding was also recorded and deserved further attention.

### Student Feedback

| Finding | Result | Responses |
|---|---:|---:|
| Preferred the 1:00–1:40 PM slot | 42.8% | 145 |
| Reported tiredness as a timing concern | 37.2% | 145 |
| Reported AC or room-temperature concerns | 38.9% | 144 |

The results highlight the importance of considering student preferences and classroom conditions when reviewing lecture schedules.

The response count differs between questions because the number of responses received for each question was not identical.

### Lecture Slot Efficiency Scores

The project used a scoring approach to compare lecture timings on a scale of 0 to 100. A score of 60 or above was considered good in the project.

| Lecture Timing | Efficiency Score | Interpretation |
|---|---:|---|
| 1:00–1:40 PM | 69.77 | Relatively stronger performance |
| 1:40–2:20 PM | 62.90 | Relatively stronger performance |
| 4:10–4:50 PM | 47.62 | Needs further review |
| 4:50–5:30 PM | 38.04 | Lower-performing slot |

These scores provide a common basis for comparing lecture timings. They should not be interpreted as direct measurements of teaching quality or proof that changing a lecture time will automatically improve attendance.

## 7. Power BI Dashboard

An interactive Power BI dashboard was developed to present the collected data and analysis in a visual format.

The dashboard helps users explore the findings without having to interpret large tables of raw data.

Its main analytical areas include:

- **Lecture Slot Analysis:** Compares efficiency scores across different lecture timings.
- **Classroom Utilization:** Presents classroom observations and recorded occupancy conditions.
- **Student Feedback:** Displays student timing preferences and reported classroom concerns.
- **Lecture Slot Efficiency:** Highlights relatively stronger and lower-scoring lecture slots.
- **SlotSense Recommendations:** Connects the analysis to possible scheduling improvements by comparing current and alternative timings.

The dashboard supports understanding of the problem, while SlotSense explores possible next steps based on the findings.

## 8. SlotSense Recommendation Prototype

**SlotSense** is a prototype developed to explore how data analysis can support possible improvements to lecture scheduling.

While the Power BI dashboard helps identify patterns and lower-scoring lecture slots, SlotSense focuses on suggesting alternative timings for further consideration.

### Information Considered

The prototype considers information such as:

- Current lecture timing
- Lecture-slot efficiency score
- Available classrooms
- Classroom capacity
- Student timing preferences
- Timetable and classroom conflicts

### How SlotSense Works

1. Identifies lecture slots with lower efficiency scores.
2. Looks for possible alternative timings.
3. Checks whether a suggested timing creates a timetable conflict.
4. Checks whether the classroom has sufficient capacity.
5. Presents possible alternatives with their corresponding efficiency scores.

The prototype uses a rule-based approach to explore feasible alternatives. It is a decision-support prototype, not a machine-learning model, and it does not automatically change the college timetable.

### Example Recommendation

The project report includes an example involving a CHE lecture in Division E.

| Parameter | Result |
|---|---|
| Subject | CHE |
| Division | E |
| Current timing | 6:10–6:50 PM |
| Current score | 39.62 |
| Suggested timing | 1:40–2:20 PM |
| Suggested score | 62.90 |
| Difference in score | +23.28 points |

In this example, the proposed alternative has a higher efficiency score than the current slot.

The recommendation is a suggestion for review, not a confirmed timetable change. The college would need to evaluate the alternative against its complete scheduling requirements before implementation.

## 9. Project Outcomes

The project resulted in the following:

- Collected 200 student survey responses.
- Completed 120 classroom observations.
- Organized and prepared the collected data for analysis.
- Identified patterns in lecture timing preferences and classroom conditions.
- Compared lecture timings using efficiency scores.
- Developed an interactive Power BI dashboard.
- Built the SlotSense recommendation prototype.
- Explored possible scheduling alternatives for further evaluation.

The project demonstrates how data analysis and visualization can help examine a practical problem and support evidence-based decision-making.

## 10. Limitations

The findings and recommendations should be considered in light of the following limitations:

- Classroom observations cover only the rooms and periods included in the fieldwork.
- Student survey responses may not represent the experience of every student.
- Efficiency scores depend on the factors and scoring rules used in the project.
- Suggested alternatives require further checks against the complete timetable and faculty availability.
- SlotSense proposes alternatives but does not automatically implement scheduling changes.
- The real-world effect of the recommendations has not been established and would need to be evaluated before drawing conclusions about their impact.

## 11. Future Improvements

Possible future improvements include:

1. Collecting classroom observations across more rooms, days, and lecture periods.
2. Including additional information about faculty availability and scheduling requirements.
3. Testing SlotSense against more timetable combinations.
4. Improving comparisons between existing and proposed timetables.
5. Working with college administrators to evaluate the practicality of recommendations.
6. Testing selected changes through a pilot before introducing them into the actual timetable.

These improvements could help assess the usefulness of the recommendations in real scheduling decisions.

## 12. Tools Used

- **Google Forms:** Student survey collection.
- **Microsoft Excel:** Data organization and preparation.
- **Microsoft Power BI:** Dashboard creation and data visualization.
- **SlotSense:** Rule-based lecture-slot recommendation prototype.
- **Microsoft Word:** Project documentation.
- **Microsoft PowerPoint:** Project presentation.

## 13. Project Details

- **Programme:** B.Sc. Data Science
- **Semester:** III
- **Academic Year:** 2026–2027
- **Institution:** S.I.W.S. N.R. Swamy College of Commerce & Economics (Autonomous)
- **Project Type:** College Field Project

## 14. Conclusion

The Smart Lecture Slot Utilization and Classroom Efficiency Analysis project explores how data can be used to understand scheduling challenges in a college environment.

By combining student survey responses, classroom observations, and timetable information, the project identified patterns in lecture timing preferences, classroom conditions, and lecture-slot efficiency.

The Power BI dashboard presents the findings visually, while SlotSense provides a way to explore possible alternative lecture timings and classroom allocations.

Together, these components demonstrate a practical process of collecting data, preparing it for analysis, identifying patterns, and using the results to explore possible improvements.

The goal is to support more informed scheduling decisions while considering student preferences, classroom capacity, and timetable constraints.e solution to optimize lecture slots, improve classroom allocation, and enhance the academic experience for students and college administration.

