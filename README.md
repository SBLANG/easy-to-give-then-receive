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
- [Research](#research)
- [Maintainers](#maintainers)



## Project summary
Easy to give then receive is an innovative technology solution built with IBM watsonx.ai&#8482;&#44; to address specific United Nations Sustainable Development Goals &#40;SDGs&#41; targets in South Africa&#46;

The main purpose of the solution is to provide&#58;

- Community with a way to&#58;
  - request assistance on behalf of others&#59;
  - create a call to action to interested parties to fulfil a need when they cannot do it themselves&#59;

- Beneficiaries with&#58;
  - an easy way to articulate and express a need&#59;
  - flexibility around what kind of help they require&#44; this could be anything from a single item&#44; volunteers&#44; collections&#44; cash donations&#44; mentorship&#44; tutoring and training&#59;
  - the safety of remaining anonymous if they wish&#59;

- Benefactors with a trusted platform to&#58;
  - identify needs that match their interests by browsing requests related by SDG&#44; location, category&#59;
  - verify that requests are within a close distance of their location or in a geographic area of their choice&#59;
  - initiatives are within their means to fulfil&#59;
  - map shortlisted initiatives back to one or more related SDG&#59;
  - determine where initiatives overlap across SDGs and build proactive strategies targeted at root causes&#59;
  - view fact sheets for each initiative to validate their authenticity and cross check against their strategy&#59;
  - build an environment&#44; social and governance  &#40;ESG&#41; portfolio of related initiatives&#59;
  - generate ESG reporting based on the initiatives they have contributed to&#59;
  - register a voluntary SDG acceleration action with the United Nations&#59;

**Goal 12: Responsible Consumption and Production**

Target 12&#46;6: Encourage companies, especially large and transnational companies&#44; to adopt sustainable practices and to integrate sustainability information into their reporting cycle

Indicator: 12&#46;6&#46;1&#58; Number of companies publishing sustainability reports

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
   |Wholesale and Retail Trade&#59; Repair of Motor Vehicles and Motorcycles|3|3|15|15|16|16|9|
   |TOTAL|87|88|97|98|11|15|42|
 
Source: [https://unstats.un.org/UNSDWebsite/undatacommons/countries?p=country%2FZAF&v=dc%2Ftopic%2Fsdg_12.6.1](https://unstats.un.org/UNSDWebsite/undatacommons/countries?p=country%2FZAF&v=dc%2Ftopic%2Fsdg_12.6.1)

Philanthropography is the first application we&#39;ve built in our roadmap&#46; It&#39; an AI-enabled web and phone assistant&#44; which gathers the needs of communities and beneficiaries seeking help&#46; Philanthropography puts benefactors in proximity of need as its top priority&#44; aiming to ease the churn typically associated with bringing help to places where it's needed most&#46; Philanthropography embodies our project&#39;s vision of putting the tools in the hands of ordinary people to make a responsible&#44; sustainable&#44; and impactful difference&#46; It does this by leveraging the power of AI to help people to develop an intimate understanding and situational&#45;awareness of the local context&#44; to which they can validate their hypotheses about individual requests for assistance&#44; without the concern of worsening the situation&#44; or creating undesired consequences&#46; If you&#39;re interested in the deeply detailed research motivating our project&#44; we&#39;ve included a link to our paper at the end of the page under [Research](#Research).

## Technical implementation
### IBM watsonx™ product(s) used
- [watsonx Assistant™](https://cloud.ibm.com/catalog/services/watsonx-assistant) - the primary way to interact with the solution is through the web chat interface or the telephone number&#46; The assistant is configured to utilize [flan-t5-xl-3b](https://dataplatform.cloud.ibm.com/wx/samples/models/google/flan-t5-xl?context=wx?context=wx&audience=wdp). Read more in the research paper [Scaling Instruction-Finetuned Language Models](https://arxiv.org/abs/2210.11416)&#46; It&#39;s also responsible for keeping the conversation log per session&#44; for a limited time&#44; and excludes PII&#46; Conversation data analytics are currently collected and viewable in watsonX Assistant&#46;

- [watsonx.governance™](https://www.ibm.com/products/watsonx-governance) &#45; is presently configured for the conversational assistant AI use case&#44; which is in the development phase&#46;

### Solution architecture
![Easy to give then receive architecture overview diagram IT systems view](/assets/images/Etgtr_AOD_IT_systems_usage_scenarios_diagram.png)

|Step Label|Step Description|
|---|---|
|1|User interacts with IBM watsonx Assistant&#46;|
|2|Conversation is recorded in the conversation log provided by IBM watsonx Assistant for a temporary period&#46;|
|3|Conversation interaction allows users to ask for help&#44; and the assistant responds by providing information&#44; which may include UN SDGs answers for some questions&#44; or Google search results, when the question is beyond the scope of the assistant&#46;|
|4|IBM watsonx&#46;governance is configured to perform data analytics on conversation data for performance monitoring&#46;|
|5|Conversation data is recorded, excluding PII&#44; by IBM watsonx, for temporary retention and retrieval from the conversation log, and for generating data analytics&#46;|
|A1|User registers an account or logs in via the website&#46;|
|A2|Configured IAM to ensure on authorized users and applications are granted access via the credentials&#44; which were provisioned&#44; and the user groups and access roles granted to them&#46;|
|A3|Authorised users are provided access to AI&#45;enabled tools&#44; and extensions for analyzing data&#44; investigating hypotheses&#44; building applications&#44; integrating other software&#44; or extending the capabilities of the web application&#46;|
|B|Triggered agent&#44; which will perform extract&#44; transform, and load operations on datasets, and migrate data to persistent storage for data visualization&#44; analysis&#44; analytics&#44; predictive analytics&#44; data mining&#44; data science&#44; machine learning&#44; and defining data connections or data sources for models and notebooks&#46;|
|C|Secure database providing ACID compliance&#44; and adherence to data sovereignty and encryption requirements&#46; The database fulfils data persistence&#44; retention&#44; and backup and recovery&#46; The database is primarily accessible via authorised connections for CRUD operations in tools and applications&#46;|
|D|Telephonic channel configured via third-party Intellipeer service&#44; for interacting with IBM watsonx Assistant&#44; providing extended STT&#44; and TSS capability&#46;|
|a|User interacts with IBM watsonx Assistant&#46;|
|b|Conversation is recorded in the conversation log provided by IBM watsonx Assistant for a temporary period&#46;|
|c|Conversation interaction allows users to ask for help&#44; and the assistant responds by providing information&#44; which may include UN SDGs answers for some questions&#44; or Google search results&#44; when the question is beyond the scope of the assistant&#46;|
|d|IBM watsonx&#46;governance is configured to perform data analytics on conversation data for performance monitoring&#46;|
|e|Conversation data is recorded, excluding PII, by IBM watsonx&#44; for temporary retention and retrieval from the conversation log&#44; and for generating data analytics&#46;|
|f|Users navigate to the web application and may interact with IBM watsonx Assistant&#44; or access further content when they are logged in&#46;|
|g|Benefactors may make monetary donations via an external third&#45;party gateway&#46;|
|i|Custom extension for implementing context&#45;aware conversational assistant to answer questions related to localized SDGs&#46;|
|ii|Configured third&#45;party Google search extension to answer questions outside of the scope of IBM watsonx Assistant&#46;|
|iii|Custom extension for building applications&#44; integrations&#44; and extending the functionality of the web application&#44; using a chained multi&#45;agent generative AI&#44; which writes an article based on the specified topic&#46;|
|iv|Implementation of model to identify patterns in data distribution in specified datasets&#44; to help users to analyze datasets&#44; for gathering contextual information when deciding which initiatives meet their requirements for sponsorship and making an impact with their philanthropy&#46; May also be utilised for predictive analytics and machine learning&#46;|
|v|Implementation of a model to detect fraudulent activity by benefactors&#46; and beneficiaries&#46; May be used for predictive analytics&#44; and machine learning&#46;|




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

# Research
To read more about the research behind our project, our paper is viewable [here](https://1drv.ms/b/c/5dbc09dff0a57015/EbK1mor_h7lEsld0bzmV5E8B2u0lV-45KwIbRcQDOt_yKQ). Our project's vision incorporates our findings, and our aspirations for further research, comprising expert systems to help philanthropists to give impactfully, while lowering any uncertainty about residual and undesired affects.

# Maintainers
@chong-cherilyn
   - product manager
   - full stack web/cloud developer
   - integration developer
   - AI/ML engineer
   - data scientist
   - UI/UX designer
   - business analyst
   - design thinking
   - designer

@SBLANG
   - product manager
   - cloud architect
   - data architect
   - researcher
   - data scientist
   - spatial data analyst
   - AI/ML engineer
   - developer
   - designer

