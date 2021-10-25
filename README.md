# Smart Pots
## Customer Requirements Analysis Document
### IoT Project developed by Blahovici Andrei, Dumitrescu Delia, Ganea Antonio, Preda Mihai, Tudor Raluca, Ţifui Alexandru


## Aplication purpose
Nowadays, there is a rise in popularity for houseplants, especially among millennials. However, it is quite a challenge to continuously monitor the moisture level of home plants. At the same time, lots of discipline is needed in order to nourish plants according to their specific needs. Wouldn’t it be nice to fill up a container once a week and not have to care about watering your plants at all?

This **IoT** project aims at implementing **remote care for a potted plant** through sensors and robotics, which monitor its state.

## Application Objectives
The application objectives are as follows:
- Analyze the moisture level of the soil;
- Automatically water the soil when required (automatic irrigation);
- Provide optimal water supply based on environment and plant characteristics;
- Monitor plant by querying climatic conditions (i.e. temperature, humidity and UV levels);
- Generate visual graphs with the polled values over time;
- Provide a revival plan for underwatered/ overwatered plants.

## Target Group
### This project targets:

1. **(at home) plant owners**, who either:
are busy and want to spend less time watering and taking care of plants,
are on vacation, thus needing a system to remotely take good care of their plants, or
want to have plants as decor, but not deal with the responsibility of watering them.
2. **Plant-related business** (e.g. plant shop) **owners**, who need their plants to be nourished and want to optimize the caring process, so that a minimum number of employees is needed.

### User Stories
- As a busy individual, I want to water my plants remotely.
- As a plant owner, I want each plant to receive proper care according to its needs.
- As a person who does not pay much attention to my plants, I want to be notified when the water container of my plant is empty or almost empty.
- As a busy mother, I want to be given an estimation about when the water recipient of a plant is going to be empty.
- As a plant shop owner, I want a way to water my plants that implies minimal effort from my employees.
- As a person looking to buy a present, I want to be able to give a self-sufficient plant (so that the receiver does not have responsibilities because of that present).

# Requirements Collection
Based on what the users would ask for, the project requirements include the following:
- remotely water the plants;
- optimally choose water supply;
- notify the user when the water container needs to be filled;
- notify the user when odd behaviour has been detected;
- analyze data about plant water consumption, plot it and have it available for the user;


## Requirements Interpretation and Prioritization
### 1. Functional/ Non-functional Tasks Labeling
#### Functional Tasks
- calculate the water quantity needed for the plant to thrive 
- constantly advise the user to refill the water container;
- calculate the water quantity needed for the plant, taking into  consideration the environment conditions and the plant characteristics;
- measure plant metadata in order to detect odd behaviour;
- store data about each plant in a flower pot;

#### Non-functional Tasks
- find a way to interact with the user (develop web or mobile app)
- compute the plant metadata by a certain metric
- find a way to analyze and plot the data

### 2. Grouping Tasks (value / difficulty)
#### Frontend
1. choose frontend technology for Web App (5 / 3) - *Ţifui Alexandru*
2. define the conceptual design of the web page (5 / 2) - *Ţifui Alexandru*
3. define UI/UX (3 / 3) - *Ţifui Alexandru*
4. get plant characteristics from the user (13 / 5) - *Blahovici Andrei*
5. send the user statistics about their plants (13 / 5) - *Tudor Raluca*

#### Backend
6. choose technology for the web API and the DB (13 / 5) - *Dumitrescu Delia*
7. define endpoints for the required actions (8 / 8) - *Preda Mihai*
8. design the database (8 / 3) - *Ganea Antonio*
9. define the architecture (13 / 8) - *Preda Mihai*
10. choose the suitable network protocols (8 / 5) - *Dumitrescu Delia*
11. measure plant characteristics (13 / 5) - *Dumitrescu Delia*
12. calculate the amount of water necessary for the plant (13 / 8) - *Ganea Antonio*
13. estimate the time when the water container will be empty (13 / 5) - *Preda Mihai*
14. notify the user when the water container is empty (13 / 5) - *Ganea Antonio*
15. generate statistics about the plants (13 / 8) - *Ganea Antonio*

## Issues value / difficulty diagram

![IssuesPlot](/IssuesPlot.jpeg)