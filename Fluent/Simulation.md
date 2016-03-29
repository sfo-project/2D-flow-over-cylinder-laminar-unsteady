# CFD Simulation Case Setup

**The created CFD domain is now read into the CFD package of interest to setup the CFD simulation. It should be noted that the current tutorial has a significant difference compared to other available CFD tutorials online! This tutorial is structured and developed based on a generic and methodological approach to set up a CFD simulation. The first principals and reasonings for each setting is discussed at each step. Potential alterations and modifications to perform similar analysis for different flow conditions are also addressed and discussed. Hence, in the end user will have the capability of applying potential modifications, improvements or extending the application of the current CFD simulation to a more complex problem of interest, rather than having a one time successful run of a specific simulation with specific and strictly pre-defined boundary conditions.**

> **_In simple words: Current tutorial teaches users to fish, rather than giving them a fish._**

## Setting up a CFD simulation has following four steps:

1. ###### Setup Model/s:   
According to the physics of the flow field user will select required model/s to simulate the flow.

2. ###### Setup Working Fluid/s & Solid/s:   
User will define the physical and thermodynamical properties of the working fluid/s and solid/s in the problem.    

3. ###### Setup Boundary & Zone Conditions:    
Solving the governing equations of the flow (i.e. system of partial differential equations) requires well-defined boundary conditions within the CFD domain. These conditions are selected and defined in this step.

4. ###### Setup Solution Methods:    
In CFD simulations the governing equations of the flow are solve numerically. Based on the physics of the problem appropriate numerical schemes and solution methods are selected at this step.

In the following section the details for the above four steps for the CFD simulation setup for **insert the topic of the problem** are explained in great details. It should be noted that the path for defining conditions and other settings are provided in `command line` format. Users can access exact same settings and options by following the provided path via the tree of progress or pull down menu in ANSYS FLUENT. The summary of the steps to take for CFD simulation setup for problem of 2D laminar flow over a flat plate are as follows:

[Insert the equavalent summary of commands for your problem of interest similar to the following sample. DO NOT USE THE SAME COMMANDS as the SAMPLE]
 1-  `/define/models/steady`   
 2-  `/define/models/solver/pressure-based`    
 3-  `/define/models/viscous/laminar`    
 4-  `/define/material/change-create`    
 5-  `/define/boundary-conditions/fluid`   
 6-  `/define/boundary-conditions/velocity-inlet`    
 7-  `/define/boundary-conditions/pressure-outlet`   
 8-  `/define/boundary-conditions/pressure-outlet`   
 9-  `/define/boundary-conditions/wall`    
 10- `solve/set/discretization-schem`    
 11- `solve/set/under-relaxation`   
 12- `/solve/initialize/compute-defaults/velocity-inlet`    
 13- `solve/iterate`

Following is the step-by-step explanation for each of the above command/setting procedure:

**1. Setup Model/s:**
* 

**2. Setup Working Fluid/s & Solid/s:**  
*

**3. Setup Boundary and Zone Conditions:**    
*

**4. Setup Solution methods:**   
*

Now all boundary conditions and settings for the CFD simulation are defined. User can **initialize** the solution through an educated guess to start the iteration process: `/solve/initialize/compute-defaults/velocity-inlet`
Solution initialization would incept the flow field variables, such as velocity and pressure, based on the defined values by user. For the current problem the CFD domain is recommended to be initialize by values of velocity and pressure at the inlet.

Iteration process for solving the flow field governing equation now shall start till converged solution is obtained:`solve/iterate`. A general rule of thumb for converged solution is to have continuity residuals of 10E-3. More details about commenting on validity of solution and convergence criteria will be discussed in next section.
