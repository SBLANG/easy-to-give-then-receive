[![License](https://img.shields.io/badge/License-Apache2-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)


# easy-to-give-then-receive

- [Project summary](#project-summary)
  - [The issue we are hoping to solve](#the-issue-we-are-hoping-to-solve)
  - [How our technology solution can help](#how-our-technology-solution-can-help)
  - [Our idea](#our-idea)
- [Technology implementation](#technology-implementation)
  - [IBM watsonx product(s) used](#ibm-ai-services-used)
  <!-- - [Other IBM technology used](#other-ibm-technology-used) -->
  - [Solution architecture](#solution-architecture)
  - [Flow of our solution](#flow-of-our-solution)
- [Presentation materials](#presentation-materials)
  - [Solution demo video](#solution-demo-video)
  - [Project development roadmap](#project-development-roadmap)
- [Additional details](#additional-details)
  - [How to run the project or live demo on local](#how-to-run-the-project-or-live-demo-on-local)
    - [Prerequisites](#prerequisites)
    - [Front-end development](#front-end-development)
    - [Back-end development](#back-end-development)
  <!-- - [Live demo](#live-demo) -->
- [Research](#research)
- [Acknowledgements](#acknowledgements)
- [Maintainers](#maintainers)
- [License](#license)



## Project summary

### The issue we are hoping to solve

Many people have intentions to do good, but who can they trust to put those intentions to use? Also, people from every walk of life go through tough times and want to be able to ask for help without the red-tape or judgment - ***getting help should be as easy as asking for it***! 

Benefactors need tools to design suitable ESG portfolios, the problem is that ***coming up with sustainable solutions is complex - nobody wants to leave people worse off than they were to begin with***. 

### How our technology solution can help

**Philanthropography** is an AI-enabled web and phone assistant, ***bringing help to places where it's needed most***.

### Our idea

**Easy to give then receive** is an innovative technology solution built with IBM watsonx™, to address specific United Nations Sustainable Development Goals (SDGs) targets in South Africa.

**Philanthropography** is the first application we've built in our roadmap. It's an AI-enabled web and phone assistant, which gathers the needs of communities and beneficiaries seeking help. 

- It puts benefactors in proximity of need as its top priority, aiming to ease the churn typically associated with bringing help to places where it's needed most. 
- It embodies our project's vision of putting the tools in the hands of ordinary people to make a responsible, sustainable, and impactful difference. 
- It does this by leveraging the power of AI to help people to develop an intimate understanding and situational-awareness of the local context, to which they can validate their hypotheses about individual requests for assistance, without the concern of worsening the situation, or creating undesired consequences. 

The main purpose of the solution is to provide:

- **Community** with a way to:
  - request assistance on behalf of others;
  - create a call to action to interested parties to fulfill a need when they cannot do it themselves;

- **Beneficiaries** with:
  - an easy way to articulate and express a need;
  - flexibility around what kind of help they require, this could be anything from a single item, volunteers, collections, cash donations, mentorship, tutoring and training;
  - the safety of remaining anonymous if they wish;

- **Benefactors** with a trusted platform to:
  - identify needs that match their interests by browsing requests related by SDG, location, category;
  - verify that requests are within a close distance of their location or in a geographic area of their choice;
  - initiatives are within their means to fulfill;
  - map shortlisted initiatives back to one or more related SDG;
  - determine where initiatives overlap across SDGs and build proactive strategies targeted at root causes;
  - view fact sheets for each initiative to validate their authenticity and cross check against their strategy;
  - build an environment, social and governance  (ESG) portfolio of related initiatives;
  - generate ESG reporting based on the initiatives they have contributed to;
  - register a voluntary SDG acceleration action with the United Nations;

These are the SDGs that our solution addresses.

- **Goal 1:** No Poverty
- **Goal 2:** Zero Hunger 
- **Goal 8:** Decent Work and Economic Growth
- **Goal 9:** Industry, Innovation and Infrastructure
- **Goal 10:** Reduced Inequality
- **Goal 11:** Sustainable Cities and Communities
- **Goal 12:** Responsible Consumption and Production
- **Goal 15:** Life on Land
- **Goal 16:** Peace, Justice and Strong Institutions
- **Goal 17:** Partnerships for the Goals

> [!NOTE]
> Indicators 11.3.1, 11.3.2, as well as all indicators in Goal 17 has not reported by South Africa up to 2023. 

Our research shows the need to bring AI to the community to address SDG priorities. A real-life example is:

>In line with the United Nations Integrated Geospatial Information Framework (UN-IGIF), South Africa is adopting the framework (Letsosa and Muthumini, 2023) for SDI, which opens opportunities for further intra, and inter governmental relations, and partnerships. Key to its success, is the recognition of a bottom-up approach to ensure that local inputs are duly acknowledged a move away from the present day issues evident in the DALRRD SALGA committee proceedings (Mandela, 2024). The literature highlighted the potential of the bottom-up approach to accomplishing the extended SDI definition, in the case of community-
based adaptation (CBA), a multiscale governance approach to address flood risk through empowering communities towards urban transformation of informal settlements in Cape Town (Fox, Ziervogel and Scheba, 2023). Informal settlement residents developed a strategy of reblocking dwellings to address poor living conditions, resulting in the City of Cape Town officially adopting it into policy, following advocacy by the Informal Settlement Network (ISN) (Fox, Ziervogel and Scheba, 2023). 

Furthermore, our finding highlighted various **weaknesses in addressing needs with current systems and datasets**: 

- data formats were not standardized across systems and were incompatible; 
- data needed to be sourced from numerous sources including successful and failed registration on account of lack of academic institution license or proprietary software license required, for example commercial licenses needed to obtain authoritative datasets, albeit data from public providers; 
- metadata was omitted and locating data specifications was problematics; 
- numerous services were no longer available online on account of changes in government vendors; 
- online geo-processing failed while local machine geo-
processing was time-consuming, for example the distance matrix for Western Cape (proximity of people to education and health services) completed execution after 28 hours; 
- and literature analysis could not be repeated to obtain identical results.

If you're interested in the deeply detailed research motivating our project, we've included a link to our paper at the end of the page under [Research](#Research).

## Technology implementation
### IBM watsonx™ product(s) used
- [watsonx Assistant™](https://cloud.ibm.com/docs/watson-assistant?topic=watson-assistant-welcome-new-assistant) - the primary way to interact with the solution is through the web chat interface or the telephone number. The assistant guides the user through a series of questions to enable them to request help. The dialogue is designed to be easy for English speakers of any age to follow with both Generative AI information gathering and HAP filtering enabled, as well as autocorrection. It's also responsible for keeping the conversation log per session, for a limited time, and excludes PII. Conversation data analytics are currently collected and viewable in watsonx Assistant. A third-party Google search extension answers questions that aren't within the scope of the assistant to answer by displaying topic-specific internet search results. The telephonic channel is configured via the third-party Intellipeer service, for interacting with watsonx Assistant, providing extended STT, and TSS capability.

- [watsonx.governance™](https://www.ibm.com/products/watsonx-governance) - is presently configured for the conversational assistant AI use case, which is in the development phase.

### Solution architecture

> [!TIP]
> Blue markers in the diagram represent current features and red are in our roadmap. 

![Easy to give then receive architecture overview diagram IT systems view](/assets/images/Etgtr_AOD_IT_systems_usage_scenarios_diagram.png)

### Flow of our solution

|Step Label|Step Description|
|---|---|
|1|User interacts with IBM watsonx Assistant.|
|2|Conversation is recorded in the conversation log provided by IBM watsonx Assistant for a temporary period.|
|3|Conversation interaction allows users to ask for help, and the assistant responds by providing information, which may include UN SDGs answers for some questions, or Google search results, when the question is beyond the scope of the assistant.|
|4|IBM watsonx.governance is configured to perform data analytics on conversation data for performance monitoring.|
|5|Conversation data is recorded, excluding PII, by IBM watsonx, for temporary retention and retrieval from the conversation log, and for generating data analytics.|
|A1|User registers an account or logs in via the website.|
|A2|Configured IAM to ensure on authorized users and applications are granted access via the credentials, which were provisioned, and the user groups and access roles granted to them.|
|A3|Authorized users are provided access to AI-enabled tools, and extensions for analyzing data, investigating hypotheses, building applications, integrating other software, or extending the capabilities of the web application.|
|B|Triggered agent, which will perform extract, transform, and load operations on datasets, and migrate data to persistent storage for data visualization, analysis, analytics, predictive analytics, data mining, data science, machine learning, and defining data connections or data sources for models and notebooks.|
|C|Secure database providing ACID compliance, and adherence to data sovereignty and encryption requirements. The database fulfills data persistence, retention, and backup and recovery. The database is primarily accessible via authorized connections for CRUD operations in tools and applications.|
|D|Telephonic channel configured via third-party Intellipeer service, for interacting with IBM watsonx Assistant, providing extended STT, and TSS capability.|
|a|User interacts with IBM watsonx Assistant.|
|b|Conversation is recorded in the conversation log provided by IBM watsonx Assistant for a temporary period.|
|c|Conversation interaction allows users to ask for help, and the assistant responds by providing information, which may include UN SDGs answers for some questions, or Google search results, when the question is beyond the scope of the assistant.|
|d|IBM watsonx.governance is configured to perform data analytics on conversation data for performance monitoring.|
|e|Conversation data is recorded, excluding PII, by IBM watsonx, for temporary retention and retrieval from the conversation log, and for generating data analytics.|
|f|Users navigate to the web application and may interact with IBM watsonx Assistant, or access further content when they are logged in.|
|g|Benefactors may make monetary donations via an external third-party gateway.|
|i|Custom extension for implementing context-aware conversational assistant to answer questions related to localized SDGs.|
|ii|Configured third-party Google search extension to answer questions outside of the scope of IBM watsonx Assistant.|
|iii|Custom extension for building applications, integrations, and extending the functionality of the web application, using a chained multi-agent generative AI, which writes an article based on the specified topic.|
|iv|Implementation of model to identify patterns in data distribution in specified datasets, to help users to analyze datasets, for gathering contextual information when deciding which initiatives meet their requirements for sponsorship and making an impact with their philanthropy. May also be utilized for predictive analytics and machine learning.|
|v|Implementation of a model to detect fraudulent activity by benefactors. and beneficiaries. May be used for predictive analytics, and machine learning.|

<details>

<summary>Underlying Architectural Principles</summary>

#### Architectural Principles

|**Principle**|**Rationale**|**Implication**|
|---|---|---|
|**Responsibility**|In order that the solution maintains a posture of responsibility, all derivative works, and activities should adhere to established guidelines, or initiate establishment of new ones.|Deviating from rules and guidelines introduces risk, which consumes resources, which should have been utilized for growth and development.|
|**Accessibility**|Access is chiefly required to advance the vision of impacting human development and the encompassing environment positively.|Notwithstanding the risk of diluting impact, sidelining accessibility may amplify existing marginalization or create others, including complex nuances therein.|
|**Ephemeral first**|Adherence to ephemeral first is mandatory to maintain the accessibility of the system to an equitable user base; additionally it may improve the resource footprint.|Omitting this objective may render the system unaffordable, or inaccessible, or impractical in terms of resource utilization.|

-  Any matters related to country regulatory compliance, legislation, laws, and policies are to be held in high regard. Responsible technology pertains to all aspects in the development of the software solutions, and engagement between stakeholders, however it excludes end-users.
-  Products, services, and activities are to be regarded as a primary mode of interaction with end-users, which should strive to be reachable to the widest audience.
-  Ephemeral comprises any component, which may be eligible for shutting down, without unmanageable impact; however this excludes business operations and user processes, as it's limited to system architecture.

</details>

## Presentation materials

### Solution demo video

[![Watch the video](assets/images/thumb.jpg)](https://vimeo.com/1020368296?share=copy)

### Project development roadmap

The project currently does the following things.

- Users interact with IBM watsonx Assistant and messages are recorded in the conversation log for a temporary period.

- Users ask for help by answering the assistant’s questions. The assistant also answers UN SDGs question and offers Google search results when the question is beyond its scope.

- With IBM watsonx.governance, data analysis is done on conversation data to monitor performance.

- Conversation data, excluding PII is recorded by IBM watsonx for temporary retention and retrieval from the conversation log, and to generate data analytics.

In the future we plan to...

#### Modularization and Mobilization

- We are starting the process of breaking our solution  down into sub-projects. 

- We will be migrating from single to multi-cloud architecture, implementing the beneficiary, citizen, benefactor and operator MVP. 

- We will be launching open innovation, launching geospatial and AI toolkits, introducing a payment gateway and creating models to detect fraud and invalid requests for help. 

This phase will run over the next 12 to 18 months. 

#### Accessibility and Empowerment

- In future, we will be migrating to micro-services, hybrid, multi-cloud architecture. 

- We will be implementing an always-on population survey, implementing an extension marketplace whilst expanding solutions to accommodate accessibility (voice-enabled with TTS and STT, VR, AR), as well as support additional platforms and channels. 

This phase will run over 18 months and we expect some overlap with the modularization and mobilization phase, especially with the accessibility accommodations. 
Citizen Sustainability
This phase is ongoing. 

#### Citizen Sustainability

We will continue our journey toward an event-driven architecture, giving community tools needed to evaluate and make decisions and implementing the latest technologies. 

Just as we take for granted to AI-embedded solutions in our home and businesses, our dream is create AI-embedded ESG. 

This is our proposed schedule on next steps after Call for Code 2024 submission.

![Roadmap](/assets/images/Project%20Development%20Roadmap.png)


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

-->

## Additional details

### How to run the project or live demo on local

#### Prerequisites

First, make sure you have your environment ready. This includes installing the relevant software applications, registering accounts for web-based tools, setting up your software, as well as forking or cloning the code repository. 

#### Software Requirements

Ideally, the following software packages should be downloaded and installed on your laptop or PC before you to start development. 

1. [Visual Studio Code](https://code.visualstudio.com/Download) (VS Code) code editor for development. 

2. [Git](https://git-scm.com/download) Source Code Management (SCM) tool and Version Control System (VCS) .

3. [Node.js](https://nodejs.org/en/download/prebuilt-installer) asynchronous, event-driven JavaScript runtime environment. 

You can choose an alternative source code editor if you prefer to however, this guideline is written for Visual Studio Code.

#### Accounts

1. Register a [GitHub](https://github.com/join) account if you haven’t done so already, which we use as our code repository and version control system.

#### Software Setup

Follow these guidelines to get your development environment set up to start contributing to the Philanthropography web app.  

##### Create a Node.js Profile
1. Open Visual Studio Code. 

2. Go to *File > Preferences > Profiles > Create Profile*.

3. Type in a name for your new profile, select Node.js as the Profile Template from the Copy from: drop-down list, choose an icon if desired and click the Create button.

The Node.js profile comes with the following extensions: 

- [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) - Integrates ESLint JavaScript into VS Code.

- [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) - Create custom development environments inside a Docker container.

- [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker) - Create, manage, and debug containerized applications.

- [DotENV](https://marketplace.visualstudio.com/items?itemName=mikestead.dotenv) - Support for dotenv file syntax.

- [EditorConfig for VS Code](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig) - EditorConfig Support for Visual Studio Code.

- [JavaScript (ES6) code snippets](https://marketplace.visualstudio.com/items?itemName=xabikos.JavaScriptSnippets) - Code snippets for JavaScript in ES6 syntax.

- [Jest](https://marketplace.visualstudio.com/items?itemName=Orta.vscode-jest) - Use Facebook's jest testing framework.

- [Microsoft Edge Tools for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-edgedevtools.vscode-edge-devtools) - Use the Microsoft Edge Tools from within VS Code.

- [npm Intellisense](https://marketplace.visualstudio.com/items?itemName=christian-kohler.npm-intellisense) - Autocomplete npm modules in import statements.

- [Prettier - Code formatter](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) - Code formatter using Prettier.

- [Rest Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) - REST Client for Visual Studio Code.

- [YAML](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) - YAML language support with built-in Kubernetes syntax.

Learn more about VS Code profiles at https://code.visualstudio.com/docs/editor/profiles. 

##### Install EJS language support extension from DigitalBrainstem

1. Click on the extensions icon in the *Activity bar* (left menu of VS Code) and type “ejs” into the search input.

2. Click the blue *Install* button to the bottom right of the EJS language support extension. 

Learn more about VS Code extensions at https://code.visualstudio.com/docs/editor/extension-marketplace.

##### Select a default VS Code terminal profile

1. Go to *Terminal > New Terminal* to open a new terminal window.

2. Click on the arrow next to the plus sign to the top right.

3. Click *Select Default Profile*.

4. Choose Git Bash from the *Command Palette* options.

5. Click the bin icon to kill the terminal.

Learn more about VS Code terminal profiles at https://code.visualstudio.com/docs/terminal/profiles.

##### Set up Git

> [!WARNING]
> Make sure you already have Git installed on your computer as well as an active Github account. 

1. Sign into VS Code using your GitHub account in the bottom right of the Activity bar (left menu of VS Code). 

Learn more about setting up your Git at https://code.visualstudio.com/docs/sourcecontrol/intro-to-git. 

##### Check for existing SSH keys and/ or generate a new SSH key

1. Go to *Terminal > New Terminal* to open a new Git Bash terminal window.

2. Place the text below to see if existing SSH keys exist to get a listing of existing keys. 

```
ls -al ~/.ssh
```

If you get this error, you don’t have an existing SSH key pair in the default location.

```
~/.ssh doesn't exist
```

If the listing contains any of the following file names, which are supported public keys for GitHub, you already have one. 

- *id_rsa.pub*

- *id_ecdsa.pub*

- *id_ed25519.pub*

> [!NOTE]
> Either reuse the existing key and skip to the next step or continue on to generate a new key. 
> Learn more about checking for existing SSH keys at https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys#checking-for-existing-ssh-keys.   
 
3. Paste the text below, replacing the email used in the example with your GitHub email address.

```
ssh-keygen -t ed25519 -C "your_email@example.com"
```
> [!WARNING]
> If you are using a legacy system that doesn't support the Ed25519 algorithm, use:

```
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

This creates a new SSH key, using the provided email as a label. The terminal prompt will display as follows: 

```
> Generating public/private ALGORITHM key pair.
```

4. When prompted to Enter a file in which to save the key, press Enter to accept the default file location. 

```
> Enter file in which to save the key (/c/Users/YOU/.ssh/id_ALGORITHM):[Press enter]
```
5. If you created SSH keys previously, ssh-keygen may ask you to rewrite another key. Rather create a custom-named SSH key. To do so, type the default file location and replace id_ALGORITHM with your custom key name.

6. At the prompt, type a secure passphrase. 

```
> Enter passphrase (empty for no passphrase): [Type a passphrase]
> Enter same passphrase again: [Type passphrase again]
```

> [!NOTE]
> Learn more about generating new SSH keys at https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=windows#generating-a-new-ssh-key.  


#### Clone the repository
1. Either run Git: Clone in the *command palette* or select *Clone Repository* from the *Source Control* view.

2. Enter the repository URL and select clone.

3.  Choose a folder on your local machine to clone the files into.

> [!NOTE]
> Learn more about source control in VS Code at https://code.visualstudio.com/docs/sourcecontrol/overview. 

#### Install dependencies and devdependencies

1. Making sure you’re in the project folder in VS Code paste the following into the Git Bash terminal to install dependencies. 

```
npm install
```

2. Paste the following into the terminal, replacing <dev_dependencies> with the module name you’re installing. 

```
npm install <dev_dependencies> --save-dev 
```

#### Run the project on local

1. Paste the following into the Git Bash terminal. 

```
npm start
```

2. Open local host 3000 to preview the web app. 

#### Front-end Development

The web app is designed using **CoreUI Bootstrap**. 

Design: 

1. Avoid making changes to the core variables directly. 

2. Override, add, remove maps or variables and create custom code in the *custom.scss* file under *demoapp > scss*. 

3. A full list of variables can be found in the *variables.scss* file under *demoapp > node_modules > @coreui > coreui > scss*. 

> [!NOTE]
> Learn more about CoreUI at https://coreui.io/bootstrap/docs/getting-started/introduction/. 


Functionality:

1. You will find existing EJS files to update under *demoapp > views*. 

2. Add new pages under *demoapp > views*. 

3. Add new partials under *demoapp > views > partials*. 

> [!NOTE]
> Learn more about EJS at https://ejs.co/#docs. 

#### Back-End Development

The web app server side is built in **JavaScript** using **Node.js**, **Express** and **Body Parser**. 

1. Open *app.js* under *demoapp > views* to add pages, integrate APIs, databases etc. to the main application. 

2. If you import any new modules, make sure to add their associated copyright and license information to *THIRDPARTY.txt* in the demoapp project folder. 

> [!NOTE]
> Learn more about Node.js at https://nodejs.org/docs/latest/api/. Learn more about Express at https://expressjs.com/en/5x/api.html. Learn more about body-parser at https://www.npmjs.com/package/body-parser.

# Research
To read more about the research behind our project, our paper is viewable [here](https://1drv.ms/b/c/5dbc09dff0a57015/EbK1mor_h7lEsld0bzmV5E8B2u0lV-45KwIbRcQDOt_yKQ). Our project's vision incorporates our findings, and our aspirations for further research, comprising expert systems to help philanthropists to give impactfully, while lowering any uncertainty about residual and undesired affects.

# Acknowledgements

We would like to thank the [Joint Research Centre](https://commission.europa.eu/about-european-commission/departments-and-executive-agencies/joint-research-centre_en) (JRC) and [Director-General for International Partnerships](https://commission.europa.eu/about-european-commission/departments-and-executive-agencies/international-partnerships_en) (DG INTPA) for the use of the [SDG Mapper Tool](https://knowsdgs.jrc.ec.europa.eu/sdgmapper). 

We would also like to acknowledge the efforts of parties who have made our work possible, including those referenced in our research paper.

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

# License
This project is licensed under the Apache 2 License - see the [LICENSE](LICENSE) file for details.