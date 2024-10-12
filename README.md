[![License](https://img.shields.io/badge/License-Apache2-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)


# easy-to-give-then-receive

- [Project summary](#project-summary)
- [Technical implementation](#technology-implementation)
  - [IBM watsonx product(s) used](#ibm-ai-services-used)
  <!-- - [Other IBM technology used](#other-ibm-technology-used) -->
  - [Solution architecture](#solution-architecture)
<!-- - [Presentation materials](#presentation-materials)
  - [Solution demo video](#solution-demo-video)
  - [Project development roadmap](#project-development-roadmap)
- [Additional details](#additional-details)
  - [How to run the project](#how-to-run-the-project)
  - [Live demo](#live-demo) -->
- [Maintainers](#maintainers)



## Project summary
Easy to give then receive is an innovative technology solution built with IBM watsonx.ai™, to address specific United Nations Sustainable Development Goals (SDGs) targets in South Africa.

The main purpose of the solution is to provide:

- Community with a way to:
   - request assistance on behalf of others;
   - create a call to action to interested parties to fulfil a need when they cannot do it themselves;

- Beneficiaries with:
   - an easy way to articulate and express a need;
   - flexibility around what kind of help they require, this could be anything from a single item, volunteers, collections, cash donations, mentorship, tutoring and training;
   - the safety of remaining anonymous if they wish;

- Benefactors with a trusted platform to:
   - identify needs that match their interests by browsing requests related by SDG, location, category;
   - verify that requests are within a close distance of their location or in a geographic area of their choice;
   - initiatives are within their means to fulfil;
   - map shortlisted initiatives back to one or more related SDG;
   - determine where initiatives overlap across SDGs and build proactive strategies targeted at root causes;
   - view fact sheets for each initiative to validate their authenticity and cross check against their strategy;
   - build an environment, social and governance (ESG) portfolio of related initiatives;
   - generate ESG reporting based on the initiatives they have contributed to;
   - register a voluntary SDG acceleration action with the United Nations;

**Goal 12: Responsible Consumption and Production**

Target 12.6: Encourage companies, especially large and transnational companies, to adopt sustainable practices and to integrate sustainability information into their reporting cycle

Indicator: 12.6.1: Number of companies publishing sustainability reports

   |DIMENSION|2017|2018|2019|2020|2021|2022|2023|
   |---|---|---|---|---|---|---|---|
   |Accommodation and Food Service Activities|1|1|1|1|1|1|1|
   |Administrative and Support Service Activities|1|1|1|1|1|1|1|
   |Construction|3|3|4|4|4|4|3|
   |Education|0|0|1|1|1|1|1|
   |Financial and Insurance Activities|13|13|14|14|15|15|4|
   |Human Health and Social Work Activities|2|2|2|2|2|2|2|
   |Information and Communication|4|4|5|5|5|5|4|
   |Manufacturing|22|22|22|22|22|22|6|
   |Mining and Quarrying|12|12|13|13|13|14|3|
   |Professional, Scientific and Technical Activities|4|4|4|4|4|5|4|
   |Real Estate Activities|6|7|7|8|9|11|3|
   |Transportation and Storage|1|1|1|1|1|1|1|
   |Wholesale and Retail Trade; Repair of Motor Vehicles and Motorcycles|3|3|15|15|16|16|9|
   |TOTAL|87|88|97|98|11|15|42|
   Source: [https://unstats.un.org/UNSDWebsite/undatacommons/countries?p=country%2FZAF&v=dc%2Ftopic%2Fsdg_12.6.1](https://unstats.un.org/UNSDWebsite/undatacommons/countries?p=country%2FZAF&v=dc%2Ftopic%2Fsdg_12.6.1)

Philanthropography is the first application we've built in our roadmap. It's an AI-enabled web and phone assistant, who gathers the needs of communities and beneficiaries seeking help. Philanthropography puts benefactors in proximity of need as its top priority, aiming to ease the churn traditionally associated with bringing help to places where it's needed most. We provide deeper detail, and our vision in our [GitHub Pages site]().

## Technical implementation
### IBM watsonx™ product(s) used
- [watsonx Assistant™](https://cloud.ibm.com/catalog/services/watsonx-assistant) - the primary way to interact with the solution is through the web chat interface or the telephone number. The assistant is configured to utilize [flan-t5-xl-3b](https://dataplatform.cloud.ibm.com/wx/samples/models/google/flan-t5-xl?context=wx?context=wx&audience=wdp). Read more in the research paper [Scaling Instruction-Finetuned Language Models](https://arxiv.org/abs/2210.11416)

### Solution architecture
![Easy to give then receive solution architecture](/assets/images/Etgtr-Solution-Architecture.png)

<!--

### IBM watsonx product(s) used

_INSTRUCTIONS: Included here is a list of IBM watsonx products. Remove any products you did not use. Leave only those included in your solution code. In your official submission on the Call for Code Global Challenge web site, you are required to provide details on where and how you used each IBM watsonx product so judges can review your implementation. Remove these instructions._

**watsonx products**

- [watsonx.ai](https://www.ibm.com/products/watsonx-ai) - WHERE AND HOW THIS IS USED IN OUR SOLUTION

- [watsonx.governance](https://www.ibm.com/products/watsonx-governance) - WHERE AND HOW THIS IS USED IN OUR SOLUTION

- [watsonx Assistant](https://cloud.ibm.com/catalog/services/watsonx-assistant) - WHERE AND HOW THIS IS USED IN OUR SOLUTION

### Other IBM technology used

INSTRUCTIONS: List any other IBM technology or IBM AI services used in your solution and describe how each component was used. If you can provide details on where these were used in your code, that would help the judges review your submission.

**Additional IBM AI services (Remove any that you did not use)**

- [Watson Machine Learning](https://cloud.ibm.com/catalog/services/watson-machine-learning) - WHERE AND HOW THIS IS USED IN OUR SOLUTION

- [Watson Studio](https://cloud.ibm.com/catalog/services/watson-studio) - WHERE AND HOW THIS IS USED IN OUR SOLUTION

- [Natural Language Understanding](https://cloud.ibm.com/catalog/services/natural-language-understanding) - WHERE AND HOW THIS IS USED IN OUR SOLUTION

- [Speech to Text](https://cloud.ibm.com/catalog/services/speech-to-text) - WHERE AND HOW THIS IS USED IN OUR SOLUTION

- [Text to Speech](https://cloud.ibm.com/catalog/services/text-to-speech) - WHERE AND HOW THIS IS USED IN OUR SOLUTION

- [Language Translator](https://cloud.ibm.com/catalog/services/language-translator) - WHERE AND HOW THIS IS USED IN OUR SOLUTION

### Solution architecture

REPLACE THIS EXAMPLE WITH YOUR OWN, OR REMOVE THIS EXAMPLE

Diagram and step-by-step description of the flow of our solution:

![Video transcription/translaftion app](https://developer.ibm.com/developer/tutorials/cfc-starter-kit-speech-to-text-app-example/images/cfc-covid19-remote-education-diagram-2.png)

1. The user navigates to the site and uploads a video file.
2. Watson Speech to Text processes the audio and extracts the text.
3. Watson Translation (optionally) can translate the text to the desired language.
4. The app stores the translated text as a document within Object Storage.

## Presentation materials

_INSTRUCTIONS: The following deliverables should be officially posted to your My Team > Submissions section of the [Call for Code Global Challenge resources site](https://cfc-prod.skillsnetwork.site/), but you can also include them here for completeness. Replace the examples seen here with your own deliverable links._

### Solution demo video

[![Watch the video](https://raw.githubusercontent.com/Liquid-Prep/Liquid-Prep/main/images/readme/IBM-interview-video-image.png)](https://youtu.be/vOgCOoy_Bx0)

### Project development roadmap

The project currently does the following things.

- Feature 1
- Feature 2
- Feature 3

In the future we plan to...

See below for our proposed schedule on next steps after Call for Code 2024 submission.

![Roadmap](./images/roadmap.jpg)

## Additional details

_INSTRUCTIONS: The following deliverables are suggested, but **optional**. Additional details like this can help the judges better review your solution. Remove any sections you are not using._

### How to run the project

INSTRUCTIONS: In this section you add the instructions to run your project on your local machine for development and testing purposes. You can also add instructions on how to deploy the project in production.

### Live demo

You can find a running system to test at...

See our [description document](./docs/DESCRIPTION.md) for log in credentials.

-->

# Maintainers
- @chong-cherilyn
   - full stack web/cloud developer
   - AI engineer
   - data scientist
   - UI/UX designer
   - business analyst
   - design thinking
- @SBLANG
   - cloud architect
   - data architect
   - researcher
   - data scientist
   - spatial data analyst
   - ML engineer
   - developer
