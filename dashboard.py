import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.offline as pyo
import plotly.graph_objects as go
import warnings


def embed_html(html_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()

    st.components.v1.html(html_content, height=600)


warnings.filterwarnings("ignore")


st.sidebar.title('Category Dropdown')
# First-level dropdown
option1 = st.sidebar.selectbox('Select Category:', ('Overview', 'Developer Profile', 'Technology', 'AI'))
    
if option1 == 'Developer Profile':
    # Second-level dropdown for Developer Profile
    option2 = st.sidebar.selectbox('Select Subcategory:', ('Developer roles', 'Education', 'Learning to code', 'Experience', 'Key territories', 'Demographics'))
elif option1 == 'Technology':
    # Second-level dropdown for Technology
    option2 = st.sidebar.selectbox('Select Subcategory:', ('Most popular technologies', 'Worked with vs. want to work with'))
elif option1 == 'AI':
    # Second-level dropdown for AI
    option2 = st.sidebar.selectbox('Select Subcategory:', ('Sentiment and usage', 'Developer tools'))

import streamlit as st

if option1 == 'Overview':
    st.title("2023 Developer Survey Analysis")

    st.markdown("Welcome to the 2023 Developer Survey Analysis project! Here, I've delved deep into survey data to uncover valuable insights and present them through compelling visualizations. Let's explore the key highlights:")

    st.markdown('**Key Highlights:**')
    st.write("- **Data Analysis:** I've conducted comprehensive data analysis, extracting meaningful insights from the survey dataset.")
    st.write("- **Data Visualization:** Using advanced libraries like Matplotlib and Seaborn, I've created stunning visualizations that provide a clear understanding of the survey results.")
    st.write("- **Interactivity:** The project is powered by Streamlit, allowing users to interact with the data and explore specific areas of interest effortlessly.")

    st.markdown('**Disclaimer:**')
    st.write("This project is a demonstration of my data analysis and visualization skills. It's based on publicly available data from the 2023 Developer Survey, offering valuable insights into the developer community.")

    st.markdown('**Conclusion:**')
    st.write("I invite you to explore this project, interact with the engaging visualizations, and gain deep insights into the developer landscape for 2023.")
    st.write("For the code used in this project, please visit my [GitHub Repo](https://github.com/shashikantdev3).")
    st.write("Thank you for considering my work!")




# Main content based on sidebar selection
if option1 == 'Developer Profile' and option2 == 'Developer roles':
    # Content for Developer Profile
    st.title("Developer Roles")

    st.write("Many developers possess a diverse skill set and identify with multiple developer roles.")

    st.markdown("**Popular Developer Types**")

    st.write("The majority of respondents identify with common developer roles:")
    st.write("- Full-stack Developers")
    st.write("- Back-end Developers")
    st.write("- Front-end Developers")
    st.write("- Desktop/Enterprise App Developers")

    st.write("Additionally, for the first time this year, StckOverFlow included a question about developer advocates, with nearly 0.3% of respondents classifying themselves as this type of developer.")
   
    # Display the chart
    st.image('Visualization/Popular_Developer_Types.png', caption='The popular developer types based on the survey results.', use_column_width=True)


if option1 == 'Developer Profile' and option2 == 'Education':
    st.title("Education")

    st.write("Most developers (84%) have a post-secondary education, having some college or more.")

    st.title("Educational Attainment")

    st.write("Most developers have attained a Bachelor's degree (41.72%) with a quarter attaining a Master's degree (23.35%).")
    # Display the chart
    st.image('Visualization/EdLevel.png', caption='Educational attainment of the survey respondents.', use_column_width=True)

if option1 == 'Developer Profile' and option2 == 'Learning to code':
    st.title("Learning to Code")

    st.write("There are as many ways to learn to code as there are coders. Developers use a variety of tools and resources to build their skills.")

    st.markdown("**Learning How to Code**")

    st.write("Learning to code from online resources increased from 70% to 80% since the 2022 survey.")
    st.write("Respondents 18 and under are those most frequently selecting online resources (e.g., videos, blogs, forums) to learn from.")
    st.write("Respondents 25 - 34 were the top age cohort to have learned from online courses or certifications (52%) but still learn more from traditional school (55%).")

    st.image('Visualization/Learning_how_to_code.png', caption = "Learning how to code", use_column_width=True)

    # Title of the web app
    st.markdown("**Top Online Resources for Learning How to Code**")

    # Define the list of online resources
    resources = [
        "Technical Documentation",
        "Stack Overflow",
        "Blogs",
        "How-To Videos",
        "Written Tutorials",
        "Books",
        "Forums",
        "Interactive Coding Platforms",
        "Online Courses",
        "Coding Bootcamps",
    ]

    # Display the list of resources
    st.write("Like previous years, technical documentation and Stack Overflow are the top online resources people use when learning to code, with blogs rounding out the top three. Well-written documentation, an active community providing solutions, and regular posts are the trifecta of enabling people to teach themselves about a technology. Developers see value in a variety of other resources like how-to videos, written tutorials, books, forums—they piece together the resources and formats that work best for their learning style.")

    st.write("**Here are the top online resources for learning how to code:**")
    st.image('Visualization/Popularity_of_Online_Resources_for_Learning_to_Code.png', caption = 'Popularity of Online Resources for Learning to Code', use_column_width=True)

    # Conclusion
    st.write("Explore these resources to kickstart your coding journey!")

    st.markdown("**Most Popular Online Course Platforms for Learning How to Code**")


    # Display the list of popular course platforms
    st.write("Udemy maintains its place as the most popular online course or certification program for learning how to code.")
    st.write("**Here are the most popular online course platforms for learning how to code:**")
    st.image('Visualization/Popularity_of_Online_Course_Platforms_for_Learning_to_Code.png', caption='Popularity of Online Course Platforms for Learning to Code', use_column_width=True)

    # Conclusion
    st.write("Explore these popular course platforms to enhance your coding skills!")



if option1 == 'Developer Profile' and option2 == 'Experience':
    st.title("Developer Experience")

    st.write("The majority of developers are in their early to mid-career stage.")

    st.markdown("**Years Coding**")

    st.write("48% of respondents have been coding for less than ten years.")
    st.write("Australia and the United Kingdom respondents are the most experienced, with an average of 17.5 and 17 years of experience coding respectively.")

    st.image('Visualization/Years_Coding_Average_by_top_10_Countries.png',caption='Years of Coding Average_by top 10 Countries', use_column_width=True)

    st.markdown("**Years Coding Professionally**")


    st.write("A majority of respondents (71%) have been working for 14 or fewer years as professional developers, and 24% have worked 15 to 29 years.")
    st.write("This shows developers in the survey have started to skew more experienced compared to last year where 75% worked 14 or fewer years and 20% 15-29 years.")

    st.image('Visualization/Years_coding_professionally.png', caption='Years coding professionally')


    st.markdown("**Years of Professional Coding Experience by Developer Type**")

    st.write("Senior executives have the highest average years of professional coding experience (17.4), followed by desktop or enterprise applications developers (16.4) and educators (15.8).")

    st.image('Visualization/Years_of_professional_coding_experience_by_developer_type.png', caption="Years of professional coding experience by developer type", use_column_width=True)



if option1 == 'Developer Profile' and option2 == 'Key territories':
    st.title("Key Territories")

    st.write("Across the world, developers and technologists turn to Stack Overflow to gain and share knowledge. Our survey received responses from almost every country on Earth.")

    st.markdown("**Geography**")

    st.write("The United States and Germany provided the highest volume of survey responses (30% combined), followed by India and UKI (UK and Northern Ireland).")
    st.write("The top ten countries account for 60% of all respondents. Germany overtook India to move into second place this year, a reverse of 2022's placement.")
    st.write("Australia broke into the top ten, coming in at ninth and displacing Spain this year.")

    st.image('Visualization/top_10_countries.png',caption='top 10 countries', use_column_width=True)

    st.components.v1.html(open("Visualization/developers_across_the_world.html", "r").read(), width=800, height=600)

if option1 == 'Developer Profile' and option2 == 'Demographics':
    st.title("Demographics")

    st.write("Stackoverflow reduced the number of demographic questions this year, only asking about age.")

    st.markdown("**Age**")

    st.image('Visualization/age_all_respondents.png', caption="Age of all respondents", use_column_width=True)
    st.write("43% of Professional Developers are 25-34 years old.")
    st.image('Visualization/Age_distribution_of_Professional_Developer.png', caption='Age distribution of Professional Developer', use_column_width=True)
    st.write("But we see that more than half of the respondents learning to code are 18-24 years old.")
    st.image('Visualization/Learning_code_age.png', caption='Age of Respondents who are Learning to Code', use_column_width=True)
    
    

if option1 == 'Technology' and option2 == 'Most popular technologies':
    st.title("Most Popular Technologies")

    st.write("This year, we're comparing the popular technologies across three different groups: All respondents, Professional Developers, and those that are learning to code.")

    st.markdown("**Programming, Scripting, and Markup Languages**")

    st.write("In 2023, JavaScript continues its streak as the most commonly-used programming language for the eleventh consecutive year.")
    st.write("- Python has overtaken SQL as the third most commonly-used language.")
    st.image("Visualization/Programming_Scripting_and_Markup_Languages.png", caption="Popular Programming, Scripting, and Markup Languages", use_column_width=True)

    st.write('- Professional developers top three technologies are the same as last year—JavaScript, HTML/CSS, and SQL.')
    st.image("Visualization/Programming_scripting_and_markup_languages_Professional.png", caption="Popular Programming, scripting, and markup languages by Professional Developers")


    st.markdown("**Databases**")

    st.write("This year, PostgreSQL took over the first place spot from MySQL. Professional Developers are more likely than those learning to code to use PostgreSQL (50%) and those learning are more likely to use MySQL (54%). ")
    st.write("MongoDB is used by a similar percentage of both Professional Developers and those learning to code and it’s the second most popular database for those learning to code (behind MySQL).")
    st.image('Visualization/Databases_all_respondents.png',caption="Popular Databases - All Respondents", use_column_width=True)
    st.image('Visualization/Database_Professional_Developer.png', caption="Popular Databases - Professional Developer", use_column_width=True)
    st.image('Visualization/Databases_Learning_to_Code.png', caption="Popular Databases - Learning to Code", use_column_width=True)



    st.markdown("**Cloud Platforms**")

    st.markdown("AWS remains the most used cloud platform for all respondents. AWS handily makes it to the top spot, almost doubling the percentage of the second most used cloud platform for all respondents, Azure.")

    st.markdown("People learning to code are still using AWS (26%) the most but it is much more at parity amongst their top three cloud platforms **(26% Google Cloud and 25% Firebase)**. *Interestingly, Heroku was the most used cloud platform last year by those learning to code but it dropped to number five this year.*")

    st.markdown("You can see the inroads that Azure has with organizations—twice as many Professional Developers are using Azure compared to people who are learning to code (30% vs. 15%).")

    st.image('Visualization/Cloud_platform_all_respondents.png', caption="Popular Cloud Platform - All Respondents", use_column_width=True)

    st.image('Visualization/Cloud_platform_Professional_developers.png', caption="Popular Cloud Platform - Professional Developers", use_column_width=True)

    st.image('Visualization/Cloud_platform_learning_code.png', caption="Popular Cloud Platform - Learning to Code", use_column_width=True)




    st.markdown("**Web Frameworks and Technologies**")

    st.markdown("Node.js and React.js are the two most common web technologies used by all respondents.")

    st.markdown("Professional Developers use both fairly equally and those learning to code use Node.js more than React (52% vs. 48%).")

    st.markdown("jQuery and Express are the next two popular web technologies for all respondents, and jQuery is used more by Professional Developers than those learning to code (24% vs. 18%), whereas Express is used more by those learning than professionals (25% vs. 20%).")

    st.markdown("Next.js moved from 11th place in 2022 to 6th this year, likely driven by its popularity with those learning to code.")
    
    st.image('Visualization/Popular_web_framework_all_respondents.png', caption="Popular Web Framework - All Respondents", use_column_width=True)

    st.image('Visualization/Popular_web_framework_professional_developers.png', caption="Popular Web Framework - Professional Developers", use_column_width=True)

    st.image('Visualization/Popular_web_framework_learning_to_code.png', caption="Popular Web Framework - Learning to Code", use_column_width=True)
    
    st.markdown("**Other Frameworks and Libraries**")

    st.write("This year, we disaggregated .NET to be more specific, and specifically .NET (5+) is top of the list again this year for other frameworks and libraries.")
    st.write(".NET (5+) is at the top followed by NumPy and Pandas. Stack Overflow added a few new options this year as well, and RabbitMQ is fairly popular with professionals (14%).")
    st.write("Python-compatible libraries continue the trend of scoring higher in this category amongst those learning to code, like last year.")
    st.write("Interspersed amongst old favorites and new options, we see Opencv and OpenGL rise up into the top 10 list (13% and 11% respectively).")

    st.image('Visualization/Popular_other_technologies_all_respondents.png', caption="Popular Other Web framework and librares - All Respondents", use_column_width=True)

    st.image('Visualization/Popular_other_technologies_professional_developers.png', caption="Popular Other Web framework and librares - Professional Developers", use_column_width=True)

    st.image('Visualization/Popular_other_technologies_learning_to_code.png', caption="Popular Other Web framework and librares - Learning to Code", use_column_width=True)


    st.markdown('**Other tools**')
    
    st.markdown("This year, Docker is the top-used other tool amongst all respondents (53%) rising from its second place spot last year.")

    st.markdown("People learning to code are more likely to be using npm or Pip than Docker (50% and 37% respectively vs. 26%).")
    st.markdown("Both are used alongside languages that are popular with students (JavaScript and Python respectively).")

    st.image('Visualization/Popular_other_tools_all_respondents.png', caption="Popular Other tools - All Respondents", use_column_width=True)

    st.image('Visualization/Popular_other_tools_professional_developers.png', caption="Popular Other tools - Professional Developers", use_column_width=True)

    st.image('Visualization/Popular_other_tools_learning_to_code.png', caption="Popular Other tools - Learning to Code", use_column_width=True)

    st.markdown('**Integrated development environment**')

    st.markdown("Visual Studio Code remains the preferred IDE across all developers, increasing its use among those learning to code compared to professional developers (78% vs. 74%).")

    st.image('Visualization/popular_ide_all_respondents.png', caption="Popular IDE - All Respondents", use_column_width=True)

    st.image('Visualization/popular_ide_professional_developers.png', caption="Popular IDE - Professional Developers", use_column_width=True)

    st.image('Visualization/popular_ide_learning_to_code.png', caption="Popular IDE - Learning to Code", use_column_width=True)
    

    st.markdown("**Asynchronous Tools**")

    st.write("Jira and Confluence are the top two asynchronous tools amongst all developers, similar to last year.")
    st.write("But this year, a new addition to the list broke into the top three: 27% of respondents use markdown files as an asynchronous tool, followed by Trello and Notion.")

    st.image('Visualization/Popular_asynchronous_tool_all_respodents.png', caption="Popular Asynchronous tools - All Respondents", use_column_width=True)

    st.image('Visualization/Popular_asynchronous_tool_professional_developers.png', caption="Popular Asynchronous tools - Professional Developers", use_column_width=True)

    st.image('Visualization/Popular_asynchronous_tool_learning_to_code.png', caption="Popular Asynchronous tools - Learning to Code", use_column_width=True)

    st.markdown("**Synchronous Tools**")

    st.write("The three most popular synchronous tools are universal for all respondents: Microsoft Teams, Slack, and Zoom.")
    st.write("Zoom was top of the list last year but is third place this year with about 10 percentage points fewer people having worked with it in the past year.")

    st.image('Visualization/Popular_synchronous_tool_all_respodents.png', caption="Popular Synchronous tools - All Respondents", use_column_width=True)

    st.image('Visualization/Popular_asynchronous_tool_professional_developers.png', caption="Popular Synchronous tools - Professional Developers", use_column_width=True)

    st.image('Visualization/Popular_synchronous_tool_professional_developers.png', caption="Popular Synchronous tools - Learning to Code", use_column_width=True)


    st.markdown("**AI Search Tools**")
    st.markdown("This is a new section this year, and respondents' top choice for AI search tools is ChatGPT: 83% of respondents have used it in the past year. This is above and beyond the second choice of Bing AI with 20% having used it.")
    st.markdown("The hype around emerging AI search technology has room to grow while the ChatGPT competitors grow their user base; only four tools had 10% or higher selection for those that want to try it in the next year.")
    
    st.image('Visualization/Popular_ai_search_tool_all_respondents.png', caption="Popular AI Search tools - All Respondents", use_column_width=True)

    st.image('Visualization/Popular_ai_search_tool_professional_developers.png', caption="Popular AI Search tools - Professional Developers", use_column_width=True)

    st.image('Visualization/Popular_ai_search_tool_all_learning_to_code.png', caption="Popular AI Search tools - Learning to Code", use_column_width=True)

    st.markdown("**AI Developer Tools**")
    # Introduction
    st.write("In addition to inquiring about search tools this year, the Stack Overflow team also gathered insights on AI developer tools.")

    # Tool Usage Stats
    st.write("GitHub Copilot emerged as the preferred AI developer tool, with a whopping 55% of respondents reporting its usage in the past year.")
    
    st.write("Tabnine came in as the second most popular choice, chosen by 13% of developers.")
    
    st.write("Interestingly, those who are still in the learning phase tend to favor Tabnine slightly more, with 18% of them using it. In contrast, Copilot's usage among learners is slightly lower at 45%. This variance might be attributed to the associated costs of Copilot.")

    st.image('Visualization/Popular_ai_developer_tool_all_respondents.png', caption="Popular AI Developer tools - All Respondents", use_column_width=True)

    st.image('Visualization/Popular_ai_developer_tool_professional_developers.png', caption="Popular AI Developer tools - Professional Developers", use_column_width=True)

    st.image('Visualization/Popular_ai_search_tool_all_learning_to_code.png', caption="Popular AI Developer tools - Learning to Code", use_column_width=True)


if option1 == 'Technology' and option2 == 'Worked with vs. want to work with':
    st.title("Worked with vs. want to work with")

    st.write("Developers are naturally curious and interested in new technologies. Let's look at what technologies they are interested in trying based on what they are using now.")

    st.markdown("**Programming, scripting, and markup languages**")

    st.write("A lot of our top used programming languages are popular because those that use them want to use them again. JavaScript, TypeScript, and HTML/CSS users all selected these three languages as their top three they want to use next year.")
    
    # Load the CSV file
    file_path = "relationship_matrix.csv"
    df = pd.read_csv(file_path)

    # Display the DataFrame
    st.title("Programming Language Usage vs. Interest in Learning.")
    st.write("A comparison of programming languages people have worked with and those they want to learn, highlighting their interests in the software development landscape")
    st.dataframe(df)

    st.title("Programming, Scripting, and Markup Languages: Current Skills vs. Aspirations Chord Diagram")

    st.markdown("**Visualizing the Relationship Between Current Skills and Aspirations in Programming, Scripting, and Markup Languages**")

    html_file_path = 'Visualization/chord_diagram.html' 
    embed_html(html_file_path)

if option1 == 'AI' and option2 == 'Sentiment and usage':
    st.title("AI Sentiment and Usage")

    st.markdown("**AI Tools in the Development Process**")

    st.write("70% of all respondents are using or are planning to use AI tools in their development process this year.")
    st.write("Those learning to code are more likely than professional developers to be using or use AI tools (82% vs. 70%).")

    st.write("Stack Overflow asked a number of questions this year about perceptions of AI, how AI tools may or may not impact developer workflows, and more.")
    st.write("I performed analysis on the data given by Stack Overflow to gain insight into the real sentiments behind this year’s surge in AI popularity. Is it making a real impact in the way developers work or is it all hype?")

    st.image('Visualization/AI_tools_in_the_development_process_all_Respondents.png', caption="Current Use of AI tool in your development process - All Respondents", use_column_width=True)

    st.image('Visualization/AI_tools_in_the_development_process_professional_developers.png', caption="Current Use of AI tool in your development process - Professional Developers", use_column_width=True)

    st.image('Visualization/AI_tools_in_the_development_process_learning_to_code.png', caption="Current Use of AI tool in your development process - Learning to Code", use_column_width=True)


    st.markdown("**AI tool sentiment**")
    st.write("70% of all respondents are using or are planning to use AI tools in their development process this year. Those learning to code are more likely than professional developers to be using or use AI tools (82% vs. 70%).")

    st.image('Visualization/AI_tool_sentimen_all_respondents.png', caption="AI Tool Sentiment", use_column_width=True)

    
if option1 == 'AI' and option2 == 'Developer tools':
    st.title("AI Developer Tools")

    st.write("Benefits of AI Tools")

    st.write("Increasing productivity is the biggest benefit that developers see from AI tools. Speeding up learning and greater efficiency are tied for secondary benefits.")

    st.image('Visualization/Benefits_of_AI_Tools.png', caption="Benefits of AI Tools - All Respondents", use_column_width=True)
    
    st.markdown("**Accuracy of AI tools**")
    st.write("We see developers split on their trust in the accuracy of the AI output from tools. About 42% trust the accuracy of the output, while 31% are on the fence.")

    st.image('Visualization/Accuracy_of_ai_tools.png', caption="Accurace of AI Tools - All Respodents", use_column_width=True)


    st.markdown("**AI in the development workflow**")
    st.write("Those currently using AI tools mostly report benefits for writing code, while those not interested in using AI tools find this the least beneficial. This disconnect most likely is with the fundamental difference of type of developers not interested in using these tools with those that are interested and have more applicable use cases for the current functionality available.")

    st.image('Visualization/Ai_in_developement_workflow.png', caption="Use of AI in the developement Workflow - All Respodents", use_column_width=True)


    st.markdown("**AI tools next year**")
    st.write("Regardless of being a professional developer or someone learning to code, people believe that their development workflow will be different in a year because of AI tools.")
    st.write("Use of AI Tool Next Year - All Respodents")
    
    # Define the path to your HTML file
    html_file_path = "Visualization/ai_tool_next_yeay_stacked.html"

    # Embed the HTML content
    st.components.v1.html(open(html_file_path, "r").read(), width=1000, height=800)


    