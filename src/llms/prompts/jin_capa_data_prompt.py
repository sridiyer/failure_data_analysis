JINDAL_CAPA_TAGS_EXTRACTION_PROMPT = """
<ROLE>
Expert industrial engineer with expertise in steel rolling mills operations, analysis,
and failure prevention.
</ROLE>

<BACKGROUND_INFO>

--Information about a steel rolling mill facility is provided. 
--A fault called 'Cobble' is described in detail
--All information related to the causes, effect, analysis and prevention of 'cobble' is
provided.
--The background information is organized as follows:

-Information about the entire Rolling Mill Facility is provided between the tags <FACILITY_INFO> and </FACILITY_INFO>. Provides overall information about the rolling mill facility.

-Information about the fault "cobble", causes, monitoring, prevention strategeis, sensors and tags that can detect are enclosed between the tags <COBBLE_INFO> and </COBBLE_INFO>.

-Cobble occurs in a sub area of the facility known as the Twin Channel Area. Detailed information about this area is provided between the tags <TWIN_CHANNEL_AREA_INFO> and </TWIN_CHANNEL_AREA_INFO>. Provides detailed information about the Twin Channel and associated Tail Braker areas.

-Failure modes of the twin channel and tail braker are provided between tags
<FAILURE_MODE_INFO> and </FAILURE_MODE_INFO>


<FACILITY_INFO>

The Rolling Mill Zone is a facility designed to transform heated steel billets into finished bar products. The process involves several key stages:

1.  **Re-Heating Furnace (RHF) Exit Area:**
    *   **Function:** Manages the transfer of hot billets from the re-heating furnace. It includes descaling (scale removal with high-pressure water), transfer to the mill entry, and emergency billet rejection.
    *   **Key Components:** Furnace Exit Roller Table, Chain Transfer, Water Descaler, Pinch Roll, Snap Shear, Emergency Discharge Table.

2.  **Roughing Mill Area:**
    *   **Function:** The initial rolling stage where billets undergo significant cross-section reduction and initial shaping.
    *   **Key Components:** 8 Roughing Mill Stands (SHS type housingless cartridges), Crop Shear (#1), Hot Metal Detectors, Pyrometers.

3.  **Finishing Mill:**
    *   **Function:** Further rolls the material to achieve dimensions closer to the final product, managing inter-stand tension and potentially slitting the bar into multiple strands.
    *   **Key Components:** 6 Finishing Mill Stands (DOM/DVM/DCF types), Vertical Loopers (for tension control), Shear #2 (Slitter type).

4.  **Specialized Finishing/Processing Lines:**
    *   **Function:** Provides final specialized processing based on product requirements, such as high-speed finishing, quenching, and tempering.
    *   **Key Components:**
        *   **High Speed Bar Lines:** Fast Finishing Blocks (FFB), Chopping Shears, Pinch Rolls, Quenching/Tempering Water Boxes (QTB).
        *   **Small Rounds Lines:** Cropping Shears, Dividing Shears, Pinch Rolls.
        *   **Big Rounds Line:** QTB, Pinch Rolls, Dividing Shear.
        *   **FFB consists of two lines:** FFB Line #1 uses JD51A11BGV and FFB Line #2 uses JD51A21BGV.

5.  **Twin Channel and Cooling Bed Area:**
    *   **Function:** Receives bars cut to length, brakes their speed, transfers them via twin channels to the cooling bed for natural air cooling, aligns them, and prepares them for the finishing area.
    *   **Key Components:** Tail Brakers, Double Twin Channel, Cooling Bed, Lining-up Rollers.

6.  **Supporting Systems:** The entire mill relies on:
    *   **Lubrication Units:** For oil, grease, and air-oil lubrication of various components.
    *   **Hydraulic Units:** Powering adjustments, clamping, and shear operations.
    *   **Fluids Distribution Systems:** Supplying cooling water and compressed air.

7.  **Control System:** A comprehensive automation system manages all operations, including operating modes, speed control, material tracking, tension/loop control, shear operations, and emergency stops, all monitored and controlled via HMIs and control pulpits.

</FACILITY_INFO>



<TWIN_CHANNEL_AREA_INFO>
### A. Twin Channel Area

The Twin Channel area is responsible for receiving cut bars from the dividing shears (via the Tail Brakers) and discharging them alternately onto the cooling bed for cooling and alignment.

**1. Twin Channel Components:**

*   **Channel Arm Assembly:**
    *   **Semi-Cylindrical Channel Support:** Curved supports that cradle the bar during its transfer. They are suspended on both sides of the central beam.
    *   **Channel Cavities:** The guiding gap formed between the central beam and the channel supports where the bar travels.
    *   **Exit Funnel Interface:** The entry point of the channel arms, designed to receive the bar smoothly.
*   **Rotation Mechanism:**
    *   **Rotating Shaft:** The main shaft that rotates to swing the channel arm assembly, enabling the discharge of the bar onto the cooling bed.
    *   **Shaft Bearing:** Fixtures that support the rotating shaft and allow for its smooth rotation.
*   **Structural Frame:**
    *   **Central Beam:** The primary structural backbone of the twin channel, running longitudinally above the cooling bed.
    *   **Channel Support Hanger:** Components that attach the channel arms to the rotating shaft, providing suspension and correct spacing.
    *   **Support Frame:** The overall structure that holds the entire twin channel assembly in its operational position above the cooling bed.
*   **Drive System:**
    *   **Motor:** Provides the mechanical power required to rotate the shaft and actuate the movement of the channel arm assembly.
    *   **Gearbox or Coupling:** Transmits torque from the motor to the rotating shaft, ensuring the correct speed and torque for the operation.
    *   **Hydraulic power pack:** Supplies hydraulic power for the movement of the channel arm assembly.
        *   **Solenoid Coil:** An electromagnetic actuator that controls hydraulic directional valves, enabling precise movement of the hydraulic system based on control signals from the automation system.


--TWIN CHANNEL COMPONET TABLE

-- following in table format describing components, sensor and tag data of tail
breaker. Each row contains following info:

-component: component name
-sub-component: any sub component
-zone : twin channel is the zone
-description: description of the component
-generic_sensor : names of generic sensors associated with the components
-specific_sensor : names of facility specific sensors associate with the components.


--TWIN CHANNEL COMPONENTS TABLE DATA

component,sub_component,zone,description,generic_sensor,specific_sensor
Twin Channel 1 Line A Drive,Motor 1,Twin Channel,"Drives the first set of rollers/flaps for Twin Channel 1, Line A.",Speed Sensor;Torque Sensor;Current Sensor;Position Sensor (flap),TWC1A_ActualSpeed1;TWC1A_ActualTorque1;TWC1A_ActPosition1;TWC1A_ActCurrent1;M001 (motor);M001-B001 (encoder)
Twin Channel 1 Line A Drive,Motor 2,Twin Channel,"Drives the second set of rollers/flaps for Twin Channel 1, Line A.",Speed Sensor;Torque Sensor;Current Sensor;Position Sensor (flap),TWC1A_ActualSpeed2;TWC1A_ActualTorque2;TWC1A_ActPosition2;TWC1A_ActCurrent2;M004 (motor);M004-B001 (encoder)
Twin Channel 1 Line A Discharging Flap,Flap Actuator(s),Twin Channel,Opens and closes to discharge bars from Twin Channel 1, Line A to the cooling bed.,Position Sensor (encoder on gearbox),TWC1A_ActPosition1;TWC1A_ActPosition2
Twin Channel 1 Line B Drive,Motor 1,Twin Channel,"Drives the first set of rollers/flaps for Twin Channel 1, Line B.",Speed Sensor;Torque Sensor;Current Sensor;Position Sensor (flap),TWC1B_ActualSpeed1;TWC1B_ActualTorque1;TWC1B_ActPosition1;TWC1B_ActCurrent1;M002 (motor);M002-B001 (encoder)
Twin Channel 1 Line B Drive,Motor 2,Twin Channel,"Drives the second set of rollers/flaps for Twin Channel 1, Line B.",Speed Sensor;Torque Sensor;Current Sensor;Position Sensor (flap),TWC1B_ActualSpeed2;TWC1B_ActualTorque2;TWC1B_ActPosition2;TWC1B_ActCurrent2;M003 (motor);M003-B001 (encoder)
Twin Channel 1 Line B Discharging Flap,Flap Actuator(s),Twin Channel,Opens and closes to discharge bars from Twin Channel 1, Line B to the cooling bed.,Position Sensor (encoder on gearbox),TWC1B_ActPosition1;TWC1B_ActPosition2
Twin Channel 2 Line A Drive,Motor 1,Twin Channel,"Drives the first set of rollers/flaps for Twin Channel 2, Line A.",Speed Sensor;Torque Sensor;Current Sensor;Position Sensor (flap),TWC2A_ActualSpeed1;TWC2A_ActualTorque1;TWC2A_ActPosition1;TWC2A_ActCurrent1;M005 (motor);M005-B001 (encoder)
Twin Channel 2 Line A Drive,Motor 2,Twin Channel,"Drives the second set of rollers/flaps for Twin Channel 2, Line A.",Speed Sensor;Torque Sensor;Current Sensor;Position Sensor (flap),TWC2A_ActualSpeed2;TWC2A_ActualTorque2;TWC2A_ActPosition2;TWC2A_ActCurrent2;M008 (motor);M008-B001 (encoder)
Twin Channel 2 Line A Discharging Flap,Flap Actuator(s),Twin Channel,Opens and closes to discharge bars from Twin Channel 2, Line A to the cooling bed.,Position Sensor (encoder on gearbox),TWC2A_ActPosition1;TWC2A_ActPosition2
Twin Channel 2 Line B Drive,Motor 1,Twin Channel,"Drives the first set of rollers/flaps for Twin Channel 2, Line B.",Speed Sensor;Torque Sensor;Current Sensor;Position Sensor (flap),TWC2B_ActualSpeed1;TWC2B_ActualTorque1;TWC2B_ActPosition1;TWC2B_ActCurrent1;M006 (motor);M006-B001 (encoder)
Twin Channel 2 Line B Drive,Motor 2,Twin Channel,"Drives the second set of rollers/flaps for Twin Channel 2, Line B.",Speed Sensor;Torque Sensor;Current Sensor;Position Sensor (flap),TWC2B_ActualSpeed2;TWC2B_ActualTorque2;TWC2B_ActPosition2;TWC2B_ActCurrent2;M007 (motor);M007-B001 (encoder)
Twin Channel 2 Line B Discharging Flap,Flap Actuator(s),Twin Channel,Opens and closes to discharge bars from Twin Channel 2, Line B to the cooling bed.,Position Sensor (encoder on gearbox),TWC2B_ActPosition1;TWC2B_ActPosition2
Twin Channel 1 Area,Cobble Detection System,Twin Channel,Detects cobbles within Twin Channel 1 (Lines A and B).,Hot Metal Detector,TWC1A_WORK_DB.CobbleDetect;TWC1B_WORK_DB.CobbleDetect;Cobble detection in TWC-1;HMD28_TWCA_ENTRY;HMD29_TWCB_ENTRY;HMD30_TWCA_ENTRY;HMD31_TWCB_ENTRY;B101
Twin Channel 2 Area,Cobble Detection System,Twin Channel,Detects cobbles within Twin Channel 2 (Lines A and B).,Hot Metal Detector,TWC2A_WORK_DB.CobbleDetect;TWC2B_WORK_DB.CobbleDetect;Cobble detection in TWC-2;B102 (if a separate HMD system exists for TWC2, otherwise uses HMDs listed for TWC1)
Twin Channel Lubrication System,Grease System Line 1,Twin Channel,Provides grease lubrication for components of Twin Channel 1.,Pressure Switch,TWC_GREASE_PRESSURE_SWITCH_LINE-1
Twin Channel Lubrication System,Grease System Line 2,Twin Channel,Provides grease lubrication for components of Twin Channel 2.,Pressure Switch,TWC_GREASE_PRESSURE_SWITCH_LINE-2
Cooling Bed,Movable Rake Drive,Cooling Bed,"Drives the movable rake of the cooling bed, which advances the bars.",Motor Drive;Position Sensor,M001 (Cooling Bed);M002 (Cooling Bed);S101;S111;S102;S112
Cooling Bed,Bar Presence Detection,Cooling Bed,Detects the presence of bars on the cooling bed, particularly on the last notch.,Proximity Sensor,S001 (Material on last teeth)
Cooling Bed,Holding Brake Section 1,Cooling Bed,Shoe brake to hold Section 1 of the cooling bed drive shaft.,Actuator Command;Solenoid Valve,Y001 (SECT.#1 - STANDING BRAKE COMMAND - OPEN)
Cooling Bed,Holding Brake Section 2,Cooling Bed,Shoe brake to hold Section 2 of the cooling bed drive shaft.,Actuator Command;Solenoid Valve,Y002 (SECT.#2 - STANDING BRAKE COMMAND - OPEN)
Twin Channel Support Structure,Tiltable Frame,Twin Channel,Common tiltable frame for mounting twin channels, allowing them to be moved offline.,Actuator Command;Position Sensor,Y001 (TWIN CHANNEL STRUCTURE COMMAND - IN/OUT);S001 (TWIN CHANNEL STRUCTURE AT POSITION - INSERTED)
Twin Channel Support Structure,Check Valve,Twin Channel,Check valve associated with the hydraulic system for the twin channel support.,Unlock Command,Y101 (CHECK VALVE COMMAND - UNLOCK)

--TWIN CHANNEL SENSORS

sensor data of the twin channel in the form of a table. Each row contains the following
information:

-name_of_sensor: name of the specific sensor
-generic_name: generic name of the sensor,
-description: description of the sensor
-component: component the sensor is associated with
-related_sensors: any related sensors

-TWIN CHANNEL SENSORS TABLE DATA
<TWIN_CHANNEL_SENSORS>
name_of_sensor,generic_name,description,component,related_sensors
TWC1A_SpeedReference1,Twin Channel 1A Speed Reference 1,Speed reference for the first motor/drive of Twin Channel 1, Line A.,Twin Channel 1A Drive 1,TWC1A_ActualSpeed1; TWC1A_SpeedReference2; M001 (motor); M001-B001 (encoder)
TWC1A_SpeedReference2,Twin Channel 1A Speed Reference 2,Speed reference for the second motor/drive of Twin Channel 1, Line A.,Twin Channel 1A Drive 2,TWC1A_ActualSpeed2; TWC1A_SpeedReference1; M004 (motor); M004-B001 (encoder)
TWC1A_ActualSpeed1,Twin Channel 1A Actual Speed 1,Actual speed of the first motor/drive of Twin Channel 1, Line A.,Twin Channel 1A Drive 1,TWC1A_SpeedReference1; TWC1A_ActualSpeed2; M001 (motor); M001-B001 (encoder)
TWC1A_ActualSpeed2,Twin Channel 1A Actual Speed 2,Actual speed of the second motor/drive of Twin Channel 1, Line A.,Twin Channel 1A Drive 2,TWC1A_SpeedReference2; TWC1A_ActualSpeed1; M004 (motor); M004-B001 (encoder)
TWC1A_TorqueLimit1,Twin Channel 1A Torque Limit 1,Torque limit setting for the first motor/drive of Twin Channel 1, Line A.,Twin Channel 1A Drive 1 Control,TWC1A_ActualTorque1; TWC1A_TorqueLimit2
TWC1A_TorqueLimit2,Twin Channel 1A Torque Limit 2,Torque limit setting for the second motor/drive of Twin Channel 1, Line A.,Twin Channel 1A Drive 2 Control,TWC1A_ActualTorque2; TWC1A_TorqueLimit1
TWC1A_ActualTorque1,Twin Channel 1A Actual Torque 1,Actual torque of the first motor/drive of Twin Channel 1, Line A.,Twin Channel 1A Drive 1,TWC1A_TorqueLimit1; TWC1A_ActualTorque2
TWC1A_ActualTorque2,Twin Channel 1A Actual Torque 2,Actual torque of the second motor/drive of Twin Channel 1, Line A.,Twin Channel 1A Drive 2,TWC1A_TorqueLimit2; TWC1A_ActualTorque1
TWC1A_ActPosition1,Twin Channel 1A Actual Position 1,Actual position of the first discharging flap/actuator of Twin Channel 1, Line A.,Twin Channel 1A Flap Actuator 1,TWC1A_SetPosition1; TWC1A_ActPosition2
TWC1A_ActPosition2,Twin Channel 1A Actual Position 2,Actual position of the second discharging flap/actuator of Twin Channel 1, Line A (if two-stage or redundant).,Twin Channel 1A Flap Actuator 2,TWC1A_SetPosition2; TWC1A_ActPosition1
TWC1A_SetPosition1,Twin Channel 1A Set Position 1,Setpoint for the position of the first discharging flap/actuator of Twin Channel 1, Line A.,Twin Channel 1A Flap Control 1,TWC1A_ActPosition1; TWC1A_SetPosition2
TWC1A_SetPosition2,Twin Channel 1A Set Position 2,Setpoint for the position of the second discharging flap/actuator of Twin Channel 1, Line A.,Twin Channel 1A Flap Control 2,TWC1A_ActPosition2; TWC1A_SetPosition1
TWC1B_SpeedReference1,Twin Channel 1B Speed Reference 1,Speed reference for the first motor/drive of Twin Channel 1, Line B.,Twin Channel 1B Drive 1,TWC1B_ActualSpeed1; TWC1B_SpeedReference2; M002 (motor); M002-B001 (encoder)
TWC1B_SpeedReference2,Twin Channel 1B Speed Reference 2,Speed reference for the second motor/drive of Twin Channel 1, Line B.,Twin Channel 1B Drive 2,TWC1B_ActualSpeed2; TWC1B_SpeedReference1; M003 (motor); M003-B001 (encoder)
TWC1B_ActualSpeed1,Twin Channel 1B Actual Speed 1,Actual speed of the first motor/drive of Twin Channel 1, Line B.,Twin Channel 1B Drive 1,TWC1B_SpeedReference1; TWC1B_ActualSpeed2; M002 (motor); M002-B001 (encoder)
TWC1B_ActualSpeed2,Twin Channel 1B Actual Speed 2,Actual speed of the second motor/drive of Twin Channel 1, Line B.,Twin Channel 1B Drive 2,TWC1B_SpeedReference2; TWC1B_ActualSpeed1; M003 (motor); M003-B001 (encoder)
TWC1B_TorqueLimit1,Twin Channel 1B Torque Limit 1,Torque limit setting for the first motor/drive of Twin Channel 1, Line B.,Twin Channel 1B Drive 1 Control,TWC1B_ActualTorque1; TWC1B_TorqueLimit2
TWC1B_TorqueLimit2,Twin Channel 1B Torque Limit 2,Torque limit setting for the second motor/drive of Twin Channel 1, Line B.,Twin Channel 1B Drive 2 Control,TWC1B_ActualTorque2; TWC1B_TorqueLimit1
TWC1B_ActualTorque1,Twin Channel 1B Actual Torque 1,Actual torque of the first motor/drive of Twin Channel 1, Line B.,Twin Channel 1B Drive 1,TWC1B_TorqueLimit1; TWC1B_ActualTorque2
TWC1B_ActualTorque2,Twin Channel 1B Actual Torque 2,Actual torque of the second motor/drive of Twin Channel 1, Line B.,Twin Channel 1B Drive 2,TWC1B_TorqueLimit2; TWC1B_ActualTorque1
TWC1B_ActPosition1,Twin Channel 1B Actual Position 1,Actual position of the first discharging flap/actuator of Twin Channel 1, Line B.,Twin Channel 1B Flap Actuator 1,TWC1B_SetPosition1; TWC1B_ActPosition2
TWC1B_ActPosition2,Twin Channel 1B Actual Position 2,Actual position of the second discharging flap/actuator of Twin Channel 1, Line B.,Twin Channel 1B Flap Actuator 2,TWC1B_SetPosition2; TWC1B_ActPosition1
TWC1B_SetPosition1,Twin Channel 1B Set Position 1,Setpoint for the position of the first discharging flap/actuator of Twin Channel 1, Line B.,Twin Channel 1B Flap Control 1,TWC1B_ActPosition1; TWC1B_SetPosition2
TWC1B_SetPosition2,Twin Channel 1B Set Position 2,Setpoint for the position of the second discharging flap/actuator of Twin Channel 1, Line B.,Twin Channel 1B Flap Control 2,TWC1B_ActPosition2; TWC1B_SetPosition1
TWC2A_SpeedReference1,Twin Channel 2A Speed Reference 1,Speed reference for the first motor/drive of Twin Channel 2, Line A.,Twin Channel 2A Drive 1,TWC2A_ActualSpeed1; TWC2A_SpeedReference2; M005 (motor); M005-B001 (encoder)
TWC2A_SpeedReference2,Twin Channel 2A Speed Reference 2,Speed reference for the second motor/drive of Twin Channel 2, Line A.,Twin Channel 2A Drive 2,TWC2A_ActualSpeed2; TWC2A_SpeedReference1; M008 (motor); M008-B001 (encoder)
TWC2A_ActualSpeed1,Twin Channel 2A Actual Speed 1,Actual speed of the first motor/drive of Twin Channel 2, Line A.,Twin Channel 2A Drive 1,TWC2A_SpeedReference1; TWC2A_ActualSpeed2; M005 (motor); M005-B001 (encoder)
TWC2A_ActualSpeed2,Twin Channel 2A Actual Speed 2,Actual speed of the second motor/drive of Twin Channel 2, Line A.,Twin Channel 2A Drive 2,TWC2A_SpeedReference2; TWC2A_ActualSpeed1; M008 (motor); M008-B001 (encoder)
TWC2A_TorqueLimit1,Twin Channel 2A Torque Limit 1,Torque limit setting for the first motor/drive of Twin Channel 2, Line A.,Twin Channel 2A Drive 1 Control,TWC2A_ActualTorque1; TWC2A_TorqueLimit2
TWC2A_TorqueLimit2,Twin Channel 2A Torque Limit 2,Torque limit setting for the second motor/drive of Twin Channel 2, Line A.,Twin Channel 2A Drive 2 Control,TWC2A_ActualTorque2; TWC2A_TorqueLimit1
TWC2A_ActualTorque1,Twin Channel 2A Actual Torque 1,Actual torque of the first motor/drive of Twin Channel 2, Line A.,Twin Channel 2A Drive 1,TWC2A_TorqueLimit1; TWC2A_ActualTorque2
TWC2A_ActualTorque2,Twin Channel 2A Actual Torque 2,Actual torque of the second motor/drive of Twin Channel 2, Line A.,Twin Channel 2A Drive 2,TWC2A_TorqueLimit2; TWC2A_ActualTorque1
TWC2A_ActPosition1,Twin Channel 2A Actual Position 1,Actual position of the first discharging flap/actuator of Twin Channel 2, Line A.,Twin Channel 2A Flap Actuator 1,TWC2A_SetPosition1; TWC2A_ActPosition2
TWC2A_ActPosition2,Twin Channel 2A Actual Position 2,Actual position of the second discharging flap/actuator of Twin Channel 2, Line A.,Twin Channel 2A Flap Actuator 2,TWC2A_SetPosition2; TWC2A_ActPosition1
TWC2A_SetPosition1,Twin Channel 2A Set Position 1,Setpoint for the position of the first discharging flap/actuator of Twin Channel 2, Line A.,Twin Channel 2A Flap Control 1,TWC2A_ActPosition1; TWC2A_SetPosition2
TWC2A_SetPosition2,Twin Channel 2A Set Position 2,Setpoint for the position of the second discharging flap/actuator of Twin Channel 2, Line A.,Twin Channel 2A Flap Control 2,TWC2A_ActPosition2; TWC2A_SetPosition1
TWC2B_SpeedReference1,Twin Channel 2B Speed Reference 1,Speed reference for the first motor/drive of Twin Channel 2, Line B.,Twin Channel 2B Drive 1,TWC2B_ActualSpeed1; TWC2B_SpeedReference2; M006 (motor); M006-B001 (encoder)
TWC2B_SpeedReference2,Twin Channel 2B Speed Reference 2,Speed reference for the second motor/drive of Twin Channel 2, Line B.,Twin Channel 2B Drive 2,TWC2B_ActualSpeed2; TWC2B_SpeedReference1; M007 (motor); M007-B001 (encoder)
TWC2B_ActualSpeed1,Twin Channel 2B Actual Speed 1,Actual speed of the first motor/drive of Twin Channel 2, Line B.,Twin Channel 2B Drive 1,TWC2B_SpeedReference1; TWC2B_ActualSpeed2; M006 (motor); M006-B001 (encoder)
TWC2B_ActualSpeed2,Twin Channel 2B Actual Speed 2,Actual speed of the second motor/drive of Twin Channel 2, Line B.,Twin Channel 2B Drive 2,TWC2B_SpeedReference2; TWC2B_ActualSpeed1; M007 (motor); M007-B001 (encoder)
TWC2B_TorqueLimit1,Twin Channel 2B Torque Limit 1,Torque limit setting for the first motor/drive of Twin Channel 2, Line B.,Twin Channel 2B Drive 1 Control,TWC2B_ActualTorque1; TWC2B_TorqueLimit2
TWC2B_TorqueLimit2,Twin Channel 2B Torque Limit 2,Torque limit setting for the second motor/drive of Twin Channel 2, Line B.,Twin Channel 2B Drive 2 Control,TWC2B_ActualTorque2; TWC2B_TorqueLimit1
TWC2B_ActualTorque1,Twin Channel 2B Actual Torque 1,Actual torque of the first motor/drive of Twin Channel 2, Line B.,Twin Channel 2B Drive 1,TWC2B_TorqueLimit1; TWC2B_ActualTorque2
TWC2B_ActualTorque2,Twin Channel 2B Actual Torque 2,Actual torque of the second motor/drive of Twin Channel 2, Line B.,Twin Channel 2B Drive 2,TWC2B_TorqueLimit2; TWC2B_ActualTorque1
TWC2B_ActPosition1,Twin Channel 2B Actual Position 1,Actual position of the first discharging flap/actuator of Twin Channel 2, Line B.,Twin Channel 2B Flap Actuator 1,TWC2B_SetPosition1; TWC2B_ActPosition2
TWC2B_ActPosition2,Twin Channel 2B Actual Position 2,Actual position of the second discharging flap/actuator of Twin Channel 2, Line B.,Twin Channel 2B Flap Actuator 2,TWC2B_SetPosition2; TWC2B_ActPosition1
TWC2B_SetPosition1,Twin Channel 2B Set Position 1,Setpoint for the position of the first discharging flap/actuator of Twin Channel 2, Line B.,Twin Channel 2B Flap Control 1,TWC2B_ActPosition1; TWC2B_SetPosition2
TWC2B_SetPosition2,Twin Channel 2B Set Position 2,Setpoint for the position of the second discharging flap/actuator of Twin Channel 2, Line B.,Twin Channel 2B Flap Control 2,TWC2B_ActPosition2; TWC2B_SetPosition1
TWC1A_WORK_DB.CobbleDetect,Twin Channel 1A Cobble Detection,Cobble detection status for Twin Channel 1, Line A.,Twin Channel 1A,HMD28_TWCA_ENTRY; HMD30_TWCA_ENTRY; B101 (Cobble on line 1 - JE11A01CDD)
TWC1B_WORK_DB.CobbleDetect,Twin Channel 1B Cobble Detection,Cobble detection status for Twin Channel 1, Line B.,Twin Channel 1B,HMD29_TWCB_ENTRY; HMD31_TWCB_ENTRY; B101 (Cobble on line 1 - JE11A01CDD)
TWC2A_WORK_DB.CobbleDetect,Twin Channel 2A Cobble Detection,Cobble detection status for Twin Channel 2, Line A.,Twin Channel 2A,HMD28_TWCA_ENTRY (if shared HMD for TWC1A & TWC2A); HMD30_TWCA_ENTRY (if shared HMD); B102 (Cobble on line 2 - JE11A01CDD)
TWC2B_WORK_DB.CobbleDetect,Twin Channel 2B Cobble Detection,Cobble detection status for Twin Channel 2, Line B.,Twin Channel 2B,HMD29_TWCB_ENTRY (if shared HMD for TWC1B & TWC2B); HMD31_TWCB_ENTRY (if shared HMD); B102 (Cobble on line 2 - JE11A01CDD)
TWC1A_WORK_DB.TWC_SafetyTrigger_ONS,Twin Channel 1A Safety Trigger Status,Status of the safety trigger for Twin Channel 1, Line A.,Twin Channel 1A Safety System,
TWC1B_WORK_DB.TWC_SafetyTrigger_ONS,Twin Channel 1B Safety Trigger Status,Status of the safety trigger for Twin Channel 1, Line B.,Twin Channel 1B Safety System,
TWC2A_WORK_DB.TWC_SafetyTrigger_ONS,Twin Channel 2A Safety Trigger Status,Status of the safety trigger for Twin Channel 2, Line A.,Twin Channel 2A Safety System,
TWC2B_WORK_DB.TWC_SafetyTrigger_ONS,Twin Channel 2B Safety Trigger Status,Status of the safety trigger for Twin Channel 2, Line B.,Twin Channel 2B Safety System,
TWC_GREASE_PRESSURE_SWITCH_LINE-1,Twin Channel Grease Pressure Switch Line 1,Pressure switch status for grease lubrication on Twin Channel Line 1 (likely TWC1A & 1B).,Twin Channel Grease Lubrication System,TWC_GREASE_PRESSURE_SWITCH_LINE-2
TWC_GREASE_PRESSURE_SWITCH_LINE-2,Twin Channel Grease Pressure Switch Line 2,Pressure switch status for grease lubrication on Twin Channel Line 2 (likely TWC2A & 2B).,Twin Channel Grease Lubrication System,TWC_GREASE_PRESSURE_SWITCH_LINE-1
Cobble detection in TWC-1,Cobble Detection in Twin Channel 1,General cobble detection status for Twin Channel 1 (combining 1A and 1B).,Twin Channel 1,TWC1A_WORK_DB.CobbleDetect; TWC1B_WORK_DB.CobbleDetect; B101 (from p221)
Cobble detection in TWC-2,Cobble Detection in Twin Channel 2,General cobble detection status for Twin Channel 2 (combining 2A and 2B).,Twin Channel 2,TWC2A_WORK_DB.CobbleDetect; TWC2B_WORK_DB.CobbleDetect; B102 (from p221)
TWC1A_TailSpeedInOutTB,Twin Channel 1A Tail Speed In/Out Tail Braker,Speed of the bar tail as it enters/exits the upstream tail braker, relevant for TWC1A control.,Tail Braker (feeding TWC1A) / TWC1A Control Input,
TWC1B_TailSpeedInOutTB,Twin Channel 1B Tail Speed In/Out Tail Braker,Speed of the bar tail as it enters/exits the upstream tail braker, relevant for TWC1B control.,Tail Braker (feeding TWC1B) / TWC1B Control Input,
TWC2A_TailSpeedInOutTB,Twin Channel 2A Tail Speed In/Out Tail Braker,Speed of the bar tail as it enters/exits the upstream tail braker, relevant for TWC2A control.,Tail Braker (feeding TWC2A) / TWC2A Control Input,
TWC2B_TailSpeedInOutTB,Twin Channel 2B Tail Speed In/Out Tail Braker,Speed of the bar tail as it enters/exits the upstream tail braker, relevant for TWC2B control.,Tail Braker (feeding TWC2B) / TWC2B Control Input,
TWC1A_ActCurrent1,Twin Channel 1A Actual Current 1,Actual electrical current for the first motor of Twin Channel 1, Line A.,Twin Channel 1A Drive 1,M001 (motor); TWC1A_ActualSpeed1; TWC1A_ActualTorque1
TWC1A_ActCurrent2,Twin Channel 1A Actual Current 2,Actual electrical current for the second motor of Twin Channel 1, Line A.,Twin Channel 1A Drive 2,M004 (motor); TWC1A_ActualSpeed2; TWC1A_ActualTorque2
TWC1B_ActCurrent1,Twin Channel 1B Actual Current 1,Actual electrical current for the first motor of Twin Channel 1, Line B.,Twin Channel 1B Drive 1,M002 (motor); TWC1B_ActualSpeed1; TWC1B_ActualTorque1
TWC1B_ActCurrent2,Twin Channel 1B Actual Current 2,Actual electrical current for the second motor of Twin Channel 1, Line B.,Twin Channel 1B Drive 2,M003 (motor); TWC1B_ActualSpeed2; TWC1B_ActualTorque2
TWC2A_ActCurrent1,Twin Channel 2A Actual Current 1,Actual electrical current for the first motor of Twin Channel 2, Line A.,Twin Channel 2A Drive 1,M005 (motor); TWC2A_ActualSpeed1; TWC2A_ActualTorque1
TWC2A_ActCurrent2,Twin Channel 2A Actual Current 2,Actual electrical current for the second motor of Twin Channel 2, Line A.,Twin Channel 2A Drive 2,M008 (motor); TWC2A_ActualSpeed2; TWC2A_ActualTorque2
TWC2B_ActCurrent1,Twin Channel 2B Actual Current 1,Actual electrical current for the first motor of Twin Channel 2, Line B.,Twin Channel 2B Drive 1,M006 (motor); TWC2B_ActualSpeed1; TWC2B_ActualTorque1
TWC2B_ActCurrent2,Twin Channel 2B Actual Current 2,Actual electrical current for the second motor of Twin Channel 2, Line B.,Twin Channel 2B Drive 2,M007 (motor); TWC2B_ActualSpeed2; TWC2B_ActualTorque2
TWC_GRS_WR_CYC_AUTO_TODAY,Twin Channel Grease Work Cycles Auto Today,Count of automatic grease lubrication cycles performed today for the Twin Channels.,Twin Channel Grease Lubrication System,TWC_GRS_WR_CYC_AUTO_LAST_DAY
TWC_GRS_WR_CYC_AUTO_LAST_DAY,Twin Channel Grease Work Cycles Auto Last Day,Count of automatic grease lubrication cycles performed on the previous day for the Twin Channels.,Twin Channel Grease Lubrication System,TWC_GRS_WR_CYC_AUTO_TODAY
TWC1A_BarOutOfTailBraker,Twin Channel 1A Bar Out Of Tail Braker,Signal indicating the bar has exited the upstream tail braker and is proceeding towards TWC1A.,Tail Braker (feeding TWC1A) / TWC1A Interlock,
TWC1B_BarOutOfTailBraker,Twin Channel 1B Bar Out Of Tail Braker,Signal indicating the bar has exited the upstream tail braker and is proceeding towards TWC1B.,Tail Braker (feeding TWC1B) / TWC1B Interlock,
TWC2A_BarOutOfTailBraker,Twin Channel 2A Bar Out Of Tail Braker,Signal indicating the bar has exited the upstream tail braker and is proceeding towards TWC2A.,Tail Braker (feeding TWC2A) / TWC2A Interlock,
TWC2B_BarOutOfTailBraker,Twin Channel 2B Bar Out Of Tail Braker,Signal indicating the bar has exited the upstream tail braker and is proceeding towards TWC2B.,Tail Braker (feeding TWC2B) / TWC2B Interlock,
TWC_1B_Reset_HMI,Twin Channel 1B Reset HMI Command,HMI command to reset alarms or status for Twin Channel 1, Line B.,Twin Channel 1B HMI Interface,
TWC_1A_Reset_HMI,Twin Channel 1A Reset HMI Command,HMI command to reset alarms or status for Twin Channel 1, Line A.,Twin Channel 1A HMI Interface,
TWC_2B_Reset_HMI,Twin Channel 2B Reset HMI Command,HMI command to reset alarms or status for Twin Channel 2, Line B.,Twin Channel 2B HMI Interface,
TWC_2A_Reset_HMI,Twin Channel 2A Reset HMI Command,HMI command to reset alarms or status for Twin Channel 2, Line A.,Twin Channel 2A HMI Interface,
</TWIN_CHANNEL_SENSORS>


### B. Tail Braker Area

The Tail Braker's function is to receive the bar from the dividing shear, pull it if necessary, and then brake its speed in a controlled manner before it is discharged into the Twin Channel. This ensures a smooth and safe transfer to the cooling bed.

**1. Tail Braker Components:**

*   **Pinch Roller System:**
    *   **Upper Roller:** Applies downward pressure onto the bar to assist in braking.
    *   **Lower Roller:** Supports the bar from underneath and provides grip for controlled deceleration.
    *   **Roller Bearing:** Enables smooth rotation of the pinch rollers with reduced friction.
    *   **Thrust Bearing:** Manages axial loads on the rollers, ensuring stability during operation.
*   **Pneumatic System:**
    *   **Pneumatic Cylinder:** Actuates the pinch rolls (likely the upper roller) to apply or release braking force, using compressed air.
    *   **Pneumatic Cylinder Rod:** Transmits the force from the pneumatic cylinder to the pinch roll mechanism.
    *   **Air Compressor:** (Usually a central plant system) Supplies the compressed air needed for the pneumatic system.
    *   **Pneumatic Cylinder Seals:** Maintain air pressure within the cylinder for effective actuation.
*   **Braking Disc System:** (If applicable, some tail brakers might rely solely on motor braking and pinch roller pressure)
    *   **Braking Disc:** A disc that rotates with the roller/drive; brake pads engage it to create friction.
    *   **Brake Pads:** Friction material pressed against the braking disc to slow down rotation.
    *   **Disc Housing:** Protects the braking disc and pad assembly.
    *   **Cooling Fan:** Dissipates heat generated during braking.
*   **Guide Roller System:**
    *   **Guide Rollers:** Help maintain the alignment of the bar as it passes through the tail braker.
    *   **Roller Shaft:** Axle supporting the guide rollers.
    *   **Support Bracket:** Mounts and holds the guide rollers in position.
*   **Control and Monitoring System:**
    *   **Control Unit:** (Part of the overall PLC/automation system) Executes the logic for braking sequences and speed control.
    *   **Safety Interlocks:** Ensure safe operation by preventing actions under unsafe conditions.
    *   **Solenoid Valves:** Electrically actuated valves controlling the flow of pneumatic air or hydraulic fluid for pinch roll actuation and pressure control.
*   **Driver System:**
    *   **Drive Motor:** Powers the pinch rolls, enabling them to pull the bar and provide controlled braking torque.
    *   **Speed Reducer (Gearbox):** Adjusts the motor's speed and torque to suitable levels for the pinch roll operation.
*   **Cooling System (for hydraulics/lubrication):**
    *   **Oil Cooler:** A heat exchanger to remove excess heat from hydraulic or lubrication oil, maintaining optimal operating temperatures.
    *   **Cooling Fan:** Assists the oil cooler by providing airflow for heat dissipation.
*   **Gear Box:**
    *   **Gears:** Transmit power and modify speed/torque from the motor to the pinch rollers.
    *   **Bearings:** Reduce friction within the gearbox for smooth operation of shafts and gears.
    *   **Shaft:** Transmits rotational motion within the gearbox.
*   **Lubrication Fluid System:**
    *   **Oil Pump:** Circulates lubrication fluid to bearings, gears, and potentially the cooler and filter.
    *   **Lubrication Fluid Cooler:** Cools the lubrication fluid to maintain its properties.
    *   **Lubricating Fluid:** Oil or grease used to reduce friction and wear in moving parts.
    *   **Pressure Regulator:** Maintains the correct pressure in the lubrication system.
    *   **Oil Filter:** Removes contaminants from the lubrication fluid to protect components.

--TAIL BRAKERS COMPONET TABLE

-- following in table format describing components,  sensor and tag data of tail
breaker. Each row contains following info:

-component: component name
-sub-component: any sub component
-zone : twin channel is the zone
-description: description of the component
-generic_sensor : names of generic sensors associated with the components
-specific_sensor : names of facility specific sensors associate with the components.

--TAIL BRAKERS COMPONENTS TABLE DATA

component,sub_component,zone,description,generic_sensor,specific_sensor
Tail Braker #1 Line A Motor Drive,Motor 1,Tail Braker,Drives the rolls for Line A of Tail Braker #1,Speed Sensor;Torque Sensor;Current Sensor;Position Sensor (from encoder);Temperature Sensor (windings);Overspeed Switch,TB2_1A_ActualLinearSpeed;TB2_1A_ActualSpeed;TB2_1A_ActualTorquePct;TB2_1A_MotorCurrent;M001-B001;M001-S901;M001-S912
Tail Braker #1 Line A Motor Drive,Motor 2,Tail Braker,Drives the rolls for Line A of Tail Braker #1 (if dual motor setup per line, less common for tail brakers),Speed Sensor;Torque Sensor;Current Sensor;Position Sensor (from encoder);Temperature Sensor (windings);Overspeed Switch,TB2_1A_ActualLinearSpeed;TB2_1A_ActualSpeed;TB2_1A_ActualTorquePct;TB2_1A_MotorCurrent;M002-B001 (assuming M002 is the second motor for line A, or it's M001 with dual encoder/feedback)
Tail Braker #1 Line A Roll Closing Mechanism,Pneumatic Cylinder,Tail Braker,Actuates the closing of the upper roll on the bar for Line A of Tail Braker #1.,Pressure Sensor;Position Sensor,TB2_1A_HighPressClose;TB2_1A_HighPressureAchieveTime;TB21A_ClsPressure;Y001;Y011;B011
Tail Braker #1 Line A Roll Closing Mechanism,Solenoid Valve(s),Tail Braker,Controls the pneumatic cylinder for roll closing on Line A of Tail Braker #1.,State Sensor,TB2_1A_RollsClose_solvalve_2;TB2_1A_HighPressClose_solvalve_2
Tail Braker #1 Line A Lubrication System,Oil Delivery,Tail Braker,Provides lubrication oil to Line A of Tail Braker #1.,Flow Sensor;Pressure Sensor;Temperature Sensor,S051;S011;S151;S111;TB_LUB_DeliveryOilTemperature
Tail Braker #1 Line B Motor Drive,Motor 1,Tail Braker,Drives the rolls for Line B of Tail Braker #1,Speed Sensor;Torque Sensor;Current Sensor;Position Sensor (from encoder);Temperature Sensor (windings);Overspeed Switch,TB2_1B_ActualLinearSpeed;TB2_1B_ActualSpeed;TB2_1B_ActualTorquePct;TB2_1B_MotorCurrent;M001-B001 (if shared) or M002-B001; M002-S901;M002-S912
Tail Braker #1 Line B Motor Drive,Motor 2,Tail Braker,Drives the rolls for Line B of Tail Braker #1 (if dual motor setup per line, less common for tail brakers),Speed Sensor;Torque Sensor;Current Sensor;Position Sensor (from encoder);Temperature Sensor (windings);Overspeed Switch,TB2_1B_ActualLinearSpeed;TB2_1B_ActualSpeed;TB2_1B_ActualTorquePct;TB2_1B_MotorCurrent
Tail Braker #1 Line B Roll Closing Mechanism,Pneumatic Cylinder,Tail Braker,Actuates the closing of the upper roll on the bar for Line B of Tail Braker #1.,Pressure Sensor;Position Sensor,TB2_1B_HighPressClose;TB2_1B_HighPressureAchieveTime;TB21B_ClsPressure;Y002;Y012;B012
Tail Braker #1 Line B Roll Closing Mechanism,Solenoid Valve(s),Tail Braker,Controls the pneumatic cylinder for roll closing on Line B of Tail Braker #1.,State Sensor,TB2_1B_RollsClose_solvalve_2;TB2_1B_HighPressClose_solvalve_2
Tail Braker #1 Line B Lubrication System,Oil Delivery,Tail Braker,Provides lubrication oil to Line B of Tail Braker #1.,Flow Sensor;Pressure Sensor;Temperature Sensor,S052;S012;S152;S112;TB_LUB_DeliveryOilTemperature
Tail Braker #2 Line A Motor Drive,Motor 1,Tail Braker,Drives the rolls for Line A of Tail Braker #2,Speed Sensor;Torque Sensor;Current Sensor;Position Sensor (from encoder);Temperature Sensor (windings);Overspeed Switch,TB2_2A_ActualLinearSpeed;TB2_2A_ActualSpeed;TB2_2A_ActualTorquePct;TB2_2A_MotorCurrent;M003-B001;M003-S901;M003-S912
Tail Braker #2 Line A Motor Drive,Motor 2,Tail Braker,Drives the rolls for Line A of Tail Braker #2 (if dual motor setup per line),Speed Sensor;Torque Sensor;Current Sensor;Position Sensor (from encoder);Temperature Sensor (windings);Overspeed Switch,TB2_2A_ActualLinearSpeed;TB2_2A_ActualSpeed;TB2_2A_ActualTorquePct;TB2_2A_MotorCurrent
Tail Braker #2 Line A Roll Closing Mechanism,Pneumatic Cylinder,Tail Braker,Actuates the closing of the upper roll on the bar for Line A of Tail Braker #2.,Pressure Sensor;Position Sensor,TB2_2A_HighPressClose;TB2_2A_HighPressureAchieveTime;TB22A_ClsPressure;Y003;Y013;B013
Tail Braker #2 Line A Roll Closing Mechanism,Solenoid Valve(s),Tail Braker,Controls the pneumatic cylinder for roll closing on Line A of Tail Braker #2.,State Sensor,TB2_2A_RollsClose_solvalve;TB2_2A_RollsClose_solvalve_2;TB2_2A_HighPressClose_solvalve;TB2_2A_HighPressClose_solvalve_2
Tail Braker #2 Line A Lubrication System,Oil Delivery,Tail Braker,Provides lubrication oil to Line A of Tail Braker #2.,Flow Sensor;Pressure Sensor;Temperature Sensor,S053;S013;S153;S113;TB_LUB_DeliveryOilTemperature
Tail Braker #2 Line B Motor Drive,Motor 1,Tail Braker,Drives the rolls for Line B of Tail Braker #2,Speed Sensor;Torque Sensor;Current Sensor;Position Sensor (from encoder);Temperature Sensor (windings);Overspeed Switch,TB2_2B_ActualLinearSpeed;TB2_2B_ActualSpeed;TB2_2B_ActualTorquePct;TB2_2B_MotorCurrent;M004-B001;M004-S901;M004-S912
Tail Braker #2 Line B Motor Drive,Motor 2,Tail Braker,Drives the rolls for Line B of Tail Braker #2 (if dual motor setup per line),Speed Sensor;Torque Sensor;Current Sensor;Position Sensor (from encoder);Temperature Sensor (windings);Overspeed Switch,TB2_2B_ActualLinearSpeed;TB2_2B_ActualSpeed;TB2_2B_ActualTorquePct;TB2_2B_MotorCurrent
Tail Braker #2 Line B Roll Closing Mechanism,Pneumatic Cylinder,Tail Braker,Actuates the closing of the upper roll on the bar for Line B of Tail Braker #2.,Pressure Sensor;Position Sensor,TB2_2B_HighPressClose;TB2_2B_HighPressureAchieveTime;TB22B_ClsPressure;Y004;Y014;B014
Tail Braker #2 Line B Roll Closing Mechanism,Solenoid Valve(s),Tail Braker,Controls the pneumatic cylinder for roll closing on Line B of Tail Braker #2.,State Sensor,TB2_2B_RollsClose_solvalve;TB2_2B_RollsClose_solvalve_2;TB2_2B_HighPressClose_solvalve;TB2_2B_HighPressClose_solvalve_2
Tail Braker #2 Line B Lubrication System,Oil Delivery,Tail Braker,Provides lubrication oil to Line B of Tail Braker #2.,Flow Sensor;Pressure Sensor;Temperature Sensor,S054;S014;S154;S114;TB_LUB_DeliveryOilTemperature
Tail Braker Lubrication System,Tank,Tail Braker,Stores lubrication oil for the tail brakers.,Temperature Sensor;Level Sensor,TB_LUB_TankOilTemperature
Tail Braker Lubrication System,Heater,Tail Braker,Heats the lubrication oil in the tank.,Status Sensor (On/Off),TB_LUB_HeaterOn
Tail Braker Hydraulic System,Accumulator Air Flanges,Tail Braker,Pressurized air accumulators for the tail braker hydraulic system.,Pressure Sensor,TB_ACC_IN_AIR_PRESSURE;TB_ACC_OUT_AIR_PRESSURE;S007
Tail Braker Shifting Car,Carriage,Tail Braker,Mounts the central tail brakers and allows them to be moved for maintenance.,Position Sensor;Command Actuator,S001 (On Line);S002 (Off Line);Y021 (Command)

--TAIL BRAKER SENSORS

sensor data of the tail braker in the form of a table. Each row contains the following
information:

-name_of_sensor: name of the specific sensor
-generic_name: generic name of the sensor,
-description: description of the sensor
-component: component the sensor is associated with
-related_sensors: any related sensors

-TAIL BRAKER SENSORS TABLE DATA
<TAIL_BREAKER_SENSORS>
name_of_sensor,generic_name,description,component,related_sensors
BAR_ACTUAL_ROLLING_SIZE_Scaled,Actual Bar Rolling Size Scaled,Scaled value representing the actual cross-sectional dimension of the rolled bar after processing.,Rolled Bar/Process Parameter,
TB_ACC_IN_AIR_PRESSURE,Tail Braker Accumulator Inlet Air Pressure,Air pressure at the inlet of the tail braker's hydraulic system accumulator.,Tail Braker Hydraulic System Accumulator,TB_ACC_OUT_AIR_PRESSURE; S007 (Air flanges pressure from p227)
TB_ACC_OUT_AIR_PRESSURE,Tail Braker Accumulator Outlet Air Pressure,Air pressure at the outlet of the tail braker's hydraulic system accumulator.,Tail Braker Hydraulic System Accumulator,TB_ACC_IN_AIR_PRESSURE; S007 (Air flanges pressure from p227)
TB_LUB_DeliveryOilTemperature,Tail Braker Lubrication Delivery Oil Temperature,Temperature of the lubrication oil being delivered to the tail braker components.,Tail Braker Lubrication System,TB_LUB_TankOilTemperature; TB_LUB_HeaterOn
TB_LUB_HeaterOn,Tail Braker Lubrication Heater Status,Status (On/Off) of the heater for the tail braker lubrication oil tank.,Tail Braker Lubrication System Heater,TB_LUB_TankOilTemperature; TB_LUB_DeliveryOilTemperature
TB_LUB_TankOilTemperature,Tail Braker Lubrication Tank Oil Temperature,Temperature of the oil within the tail braker lubrication system tank.,Tail Braker Lubrication System Tank,TB_LUB_DeliveryOilTemperature; TB_LUB_HeaterOn
TB2_1A_ActualLinearSpeed,Tail Braker 2 Line 1A Actual Linear Speed,Actual linear speed of Tail Braker #1 Line A rolls.,Tail Braker 1A Drive,TB2_1A_ActualSpeed; TB2_1A_SetLinearSpeed; TB2_1A_SpeedRef; M001/M002 (motor); M001-B001 (encoder)
TB2_1A_ActualSpeed,Tail Braker 2 Line 1A Actual Angular Speed,Actual angular speed of Tail Braker #1 Line A motor/rolls.,Tail Braker 1A Drive,TB2_1A_ActualLinearSpeed; TB2_1A_SetLinearSpeed; TB2_1A_SpeedRef; M001/M002 (motor); M001-B001 (encoder)
TB2_1A_ActualTorquePct,Tail Braker 2 Line 1A Actual Torque Percentage,Actual torque percentage of Tail Braker #1 Line A motor.,Tail Braker 1A Motor,TB2_1A_LimitedTorque; TB2_1A_TorqueLimitPct
TB2_1A_BarHeadPosition,Tail Braker 2 Line 1A Bar Head Position,Position of the bar's head as it passes through Tail Braker #1 Line A.,Tail Braker 1A,TB2_1A_BarTailPosition; TB2_1A_TailPos
TB2_1A_BarTailPosition,Tail Braker 2 Line 1A Bar Tail Position,Position of the bar's tail as it passes through Tail Braker #1 Line A.,Tail Braker 1A,TB2_1A_BarHeadPosition; TB2_1A_TailPos
TB2_1A_BrakingSpeedSel,Tail Braker 2 Line 1A Braking Speed Selection,Selected braking speed for Tail Braker #1 Line A.,Tail Braker 1A Control System,
TB2_1A_HighPressClose,Tail Braker 2 Line 1A High Pressure Close Status,Status of high-pressure roll closing for Tail Braker #1 Line A.,Tail Braker 1A Roll Closing Mechanism,TB2_1A_HighPressClose_solvalve_2; Y011 (command)
TB2_1A_HighPressClose_solvalve_2,Tail Braker 2 Line 1A High Pressure Close Solenoid Valve 2 State,State of the second solenoid valve for high-pressure roll closing on Tail Braker #1 Line A.,Tail Braker 1A Roll Closing Solenoid Valve,TB2_1A_HighPressClose; Y011 (command)
TB2_1A_HighPressureAchieveTime,Tail Braker 2 Line 1A High Pressure Achieve Time,Time taken to achieve high pressure for roll closing on Tail Braker #1 Line A.,Tail Braker 1A Roll Closing Mechanism,
TB2_1A_LimitedTorque,Tail Braker 2 Line 1A Limited Torque,Status indicating if torque limit is active for Tail Braker #1 Line A motor.,Tail Braker 1A Motor Control,TB2_1A_ActualTorquePct; TB2_1A_TorqueLimitPct
TB2_1A_MotorCurrent,Tail Braker 2 Line 1A Motor Current,Electrical current drawn by Tail Braker #1 Line A motor.,Tail Braker 1A Motor,M001/M002
TB2_1A_OverspeedSel,Tail Braker 2 Line 1A Overspeed Selection,Selected overspeed setting for Tail Braker #1 Line A.,Tail Braker 1A Control System,TB2_1A_ReducedOvspdSel
TB2_1A_ReducedOvspdSel,Tail Braker 2 Line 1A Reduced Overspeed Selection,Selected reduced overspeed setting for Tail Braker #1 Line A.,Tail Braker 1A Control System,TB2_1A_OverspeedSel
TB2_1A_RollsClose_solvalve_2,Tail Braker 2 Line 1A Rolls Close Solenoid Valve 2 State,State of the second solenoid valve for roll closing on Tail Braker #1 Line A.,Tail Braker 1A Roll Closing Solenoid Valve,TB2_1A_RollsCloseCmd; Y001 (command)
TB2_1A_RollsCloseCmd,Tail Braker 2 Line 1A Rolls Close Command Status,Status of the command to close rolls for Tail Braker #1 Line A.,Tail Braker 1A Control System,Y001 (command); TB2_1A_RollsClose_solvalve_2
TB2_1A_selection_valve1,Tail Braker 2 Line 1A Selection Valve 1 State,State of selection valve 1 for Tail Braker #1 Line A (likely for hydraulic/pneumatic routing).,Tail Braker 1A Hydraulic/Pneumatic System,TB2_1A_selection_valve2
TB2_1A_selection_valve2,Tail Braker 2 Line 1A Selection Valve 2 State,State of selection valve 2 for Tail Braker #1 Line A (likely for hydraulic/pneumatic routing).,Tail Braker 1A Hydraulic/Pneumatic System,TB2_1A_selection_valve1
TB2_1A_SetLinearSpeed,Tail Braker 2 Line 1A Set Linear Speed,Setpoint for the linear speed of Tail Braker #1 Line A rolls.,Tail Braker 1A Control System,TB2_1A_ActualLinearSpeed; TB2_1A_SpeedRef
TB2_1A_SpeedRef,Tail Braker 2 Line 1A Speed Reference,Speed reference signal for Tail Braker #1 Line A motor drive.,Tail Braker 1A Drive Control,TB2_1A_ActualLinearSpeed; TB2_1A_SetLinearSpeed
TB2_1A_TAIL HEAD DETACH,Tail Braker 2 Line 1A Tail Head Detach,Detection of tail head detachment at Tail Braker #1 Line A.,Tail Braker 1A Bar Detection,TB2_1A_TailPos
TB2_1A_TailPos,Tail Braker 2 Line 1A Tail Position,Position of the bar's tail at Tail Braker #1 Line A.,Tail Braker 1A,TB2_1A_BarTailPosition
TB2_1A_TailSpeedSel,Tail Braker 2 Line 1A Tail Speed Selection,Selected speed for handling the tail end of the bar at Tail Braker #1 Line A.,Tail Braker 1A Control System,
TB2_1A_TorqueLimitPct,Tail Braker 2 Line 1A Torque Limit Percentage,Setpoint for the torque limit percentage of Tail Braker #1 Line A motor.,Tail Braker 1A Motor Control,TB2_1A_ActualTorquePct; TB2_1A_LimitedTorque
TB2_1B_ActualLinearSpeed,Tail Braker 2 Line 1B Actual Linear Speed,Actual linear speed of Tail Braker #1 Line B rolls.,Tail Braker 1B Drive,TB2_1B_ActualSpeed; TB2_1B_SetLinearSpeed; M001/M002 (motor); M001-B001 (encoder)
TB2_1B_ActualSpeed,Tail Braker 2 Line 1B Actual Angular Speed,Actual angular speed of Tail Braker #1 Line B motor/rolls.,Tail Braker 1B Drive,TB2_1B_ActualLinearSpeed; TB2_1B_SetLinearSpeed; M001/M002 (motor); M001-B001 (encoder)
TB2_1B_ActualTorquePct,Tail Braker 2 Line 1B Actual Torque Percentage,Actual torque percentage of Tail Braker #1 Line B motor.,Tail Braker 1B Motor,TB2_1B_LimitedTorque; TB2_1B_TorqueLimitPct
TB2_1B_BarHeadPosition,Tail Braker 2 Line 1B Bar Head Position,Position of the bar's head as it passes through Tail Braker #1 Line B.,Tail Braker 1B,TB2_1B_BarTailPosition; TB2_1B_TailPos
TB2_1B_BarTailPosition,Tail Braker 2 Line 1B Bar Tail Position,Position of the bar's tail as it passes through Tail Braker #1 Line B.,Tail Braker 1B,TB2_1B_BarHeadPosition; TB2_1B_TailPos
TB2_1B_BrakingSpeedSel,Tail Braker 2 Line 1B Braking Speed Selection,Selected braking speed for Tail Braker #1 Line B.,Tail Braker 1B Control System,
TB2_1B_HighPressClose,Tail Braker 2 Line 1B High Pressure Close Status,Status of high-pressure roll closing for Tail Braker #1 Line B.,Tail Braker 1B Roll Closing Mechanism,TB2_1B_HighPressClose_solvalve_2; Y012 (command)
TB2_1B_HighPressClose_solvalve_2,Tail Braker 2 Line 1B High Pressure Close Solenoid Valve 2 State,State of the second solenoid valve for high-pressure roll closing on Tail Braker #1 Line B.,Tail Braker 1B Roll Closing Solenoid Valve,TB2_1B_HighPressClose; Y012 (command)
TB2_1B_HighPressureAchieveTime,Tail Braker 2 Line 1B High Pressure Achieve Time,Time taken to achieve high pressure for roll closing on Tail Braker #1 Line B.,Tail Braker 1B Roll Closing Mechanism,
TB2_1B_LimitedTorque,Tail Braker 2 Line 1B Limited Torque,Status indicating if torque limit is active for Tail Braker #1 Line B motor.,Tail Braker 1B Motor Control,TB2_1B_ActualTorquePct; TB2_1B_TorqueLimitPct
TB2_1B_MotorCurrent,Tail Braker 2 Line 1B Motor Current,Electrical current drawn by Tail Braker #1 Line B motor.,Tail Braker 1B Motor,M001/M002
TB2_1B_OverspeedSel,Tail Braker 2 Line 1B Overspeed Selection,Selected overspeed setting for Tail Braker #1 Line B.,Tail Braker 1B Control System,TB2_1B_ReducedOvspdSel
TB2_1B_ReducedOvspdSel,Tail Braker 2 Line 1B Reduced Overspeed Selection,Selected reduced overspeed setting for Tail Braker #1 Line B.,Tail Braker 1B Control System,TB2_1B_OverspeedSel
TB2_1B_RollsClose_solvalve_2,Tail Braker 2 Line 1B Rolls Close Solenoid Valve 2 State,State of the second solenoid valve for roll closing on Tail Braker #1 Line B.,Tail Braker 1B Roll Closing Solenoid Valve,TB2_1B_RollsCloseCmd; Y002 (command)
TB2_1B_RollsCloseCmd,Tail Braker 2 Line 1B Rolls Close Command Status,Status of the command to close rolls for Tail Braker #1 Line B.,Tail Braker 1B Control System,Y002 (command); TB2_1B_RollsClose_solvalve_2
TB2_1B_selection_valve1,Tail Braker 2 Line 1B Selection Valve 1 State,State of selection valve 1 for Tail Braker #1 Line B.,Tail Braker 1B Hydraulic/Pneumatic System,TB2_1B_selection_valve2
TB2_1B_selection_valve2,Tail Braker 2 Line 1B Selection Valve 2 State,State of selection valve 2 for Tail Braker #1 Line B.,Tail Braker 1B Hydraulic/Pneumatic System,TB2_1B_selection_valve1
TB2_1B_SetLinearSpeed,Tail Braker 2 Line 1B Set Linear Speed,Setpoint for the linear speed of Tail Braker #1 Line B rolls.,Tail Braker 1B Control System,TB2_1B_ActualLinearSpeed; TB2_1B_SpeedRef
TB2_1B_SpeedRef,Tail Braker 2 Line 1B Speed Reference,Speed reference signal for Tail Braker #1 Line B motor drive.,Tail Braker 1B Drive Control,TB2_1B_ActualLinearSpeed; TB2_1B_SetLinearSpeed
TB2_1B_Tail head detach when divide,Tail Braker 2 Line 1B Tail Head Detach during Dividing,Detection of tail head detachment during dividing operation at Tail Braker #1 Line B.,Tail Braker 1B Bar Detection,TB2_1B_TailPos
TB2_1B_TailPos,Tail Braker 2 Line 1B Tail Position,Position of the bar's tail at Tail Braker #1 Line B.,Tail Braker 1B,TB2_1B_BarTailPosition
TB2_1B_TailSpeedSel,Tail Braker 2 Line 1B Tail Speed Selection,Selected speed for handling the tail end of the bar at Tail Braker #1 Line B.,Tail Braker 1B Control System,
TB2_1B_TorqueLimitPct,Tail Braker 2 Line 1B Torque Limit Percentage,Setpoint for the torque limit percentage of Tail Braker #1 Line B motor.,Tail Braker 1B Motor Control,TB2_1B_ActualTorquePct; TB2_1B_LimitedTorque
TB2_2A_ActualLinearSpeed,Tail Braker 2 Line 2A Actual Linear Speed,Actual linear speed of Tail Braker #2 Line A rolls.,Tail Braker 2A Drive,TB2_2A_ActualSpeed; TB2_2A_SetLinearSpeed; M003/M004 (motor); M003-B001 (encoder)
TB2_2A_ActualSpeed,Tail Braker 2 Line 2A Actual Angular Speed,Actual angular speed of Tail Braker #2 Line A motor/rolls.,Tail Braker 2A Drive,TB2_2A_ActualLinearSpeed; TB2_2A_SetLinearSpeed; M003/M004 (motor); M003-B001 (encoder)
TB2_2A_ActualTorquePct,Tail Braker 2 Line 2A Actual Torque Percentage,Actual torque percentage of Tail Braker #2 Line A motor.,Tail Braker 2A Motor,TB2_2A_LimitedTorque; TB2_2A_TorqueLimitPct
TB2_2A_BarHeadPosition,Tail Braker 2 Line 2A Bar Head Position,Position of the bar's head as it passes through Tail Braker #2 Line A.,Tail Braker 2A,TB2_2A_BarTailPosition; TB2_2A_TailPos
TB2_2A_BarTailPosition,Tail Braker 2 Line 2A Bar Tail Position,Position of the bar's tail as it passes through Tail Braker #2 Line A.,Tail Braker 2A,TB2_2A_BarHeadPosition; TB2_2A_TailPos
TB2_2A_BrakingSpeedSel,Tail Braker 2 Line 2A Braking Speed Selection,Selected braking speed for Tail Braker #2 Line A.,Tail Braker 2A Control System,
TB2_2A_HighPressClose,Tail Braker 2 Line 2A High Pressure Close Status,Status of high-pressure roll closing for Tail Braker #2 Line A.,Tail Braker 2A Roll Closing Mechanism,TB2_2A_HighPressClose_solvalve; TB2_2A_HighPressClose_solvalve_2; Y013 (command)
TB2_2A_HighPressClose_solvalve,Tail Braker 2 Line 2A High Pressure Close Solenoid Valve State,State of the solenoid valve for high-pressure roll closing on Tail Braker #2 Line A.,Tail Braker 2A Roll Closing Solenoid Valve,TB2_2A_HighPressClose; TB2_2A_HighPressClose_solvalve_2; Y013 (command)
TB2_2A_HighPressClose_solvalve_2,Tail Braker 2 Line 2A High Pressure Close Solenoid Valve 2 State,State of the second solenoid valve for high-pressure roll closing on Tail Braker #2 Line A.,Tail Braker 2A Roll Closing Solenoid Valve,TB2_2A_HighPressClose; TB2_2A_HighPressClose_solvalve; Y013 (command)
TB2_2A_HighPressureAchieveTime,Tail Braker 2 Line 2A High Pressure Achieve Time,Time taken to achieve high pressure for roll closing on Tail Braker #2 Line A.,Tail Braker 2A Roll Closing Mechanism,
TB2_2A_LimitedTorque,Tail Braker 2 Line 2A Limited Torque,Status indicating if torque limit is active for Tail Braker #2 Line A motor.,Tail Braker 2A Motor Control,TB2_2A_ActualTorquePct; TB2_2A_TorqueLimitPct
TB2_2A_MotorCurrent,Tail Braker 2 Line 2A Motor Current,Electrical current drawn by Tail Braker #2 Line A motor.,Tail Braker 2A Motor,M003/M004
TB2_2A_OverspeedSel,Tail Braker 2 Line 2A Overspeed Selection,Selected overspeed setting for Tail Braker #2 Line A.,Tail Braker 2A Control System,TB2_2A_ReducedOvspdSel
TB2_2A_ReducedOvspdSel,Tail Braker 2 Line 2A Reduced Overspeed Selection,Selected reduced overspeed setting for Tail Braker #2 Line A.,Tail Braker 2A Control System,TB2_2A_OverspeedSel
TB2_2A_RollsClose_solvalve,Tail Braker 2 Line 2A Rolls Close Solenoid Valve State,State of the solenoid valve for roll closing on Tail Braker #2 Line A.,Tail Braker 2A Roll Closing Solenoid Valve,TB2_2A_RollsCloseCmd; Y003 (command); TB2_2A_RollsClose_solvalve_2
TB2_2A_RollsClose_solvalve_2,Tail Braker 2 Line 2A Rolls Close Solenoid Valve 2 State,State of the second solenoid valve for roll closing on Tail Braker #2 Line A.,Tail Braker 2A Roll Closing Solenoid Valve,TB2_2A_RollsCloseCmd; Y003 (command); TB2_2A_RollsClose_solvalve
TB2_2A_RollsCloseCmd,Tail Braker 2 Line 2A Rolls Close Command Status,Status of the command to close rolls for Tail Braker #2 Line A.,Tail Braker 2A Control System,Y003 (command); TB2_2A_RollsClose_solvalve; TB2_2A_RollsClose_solvalve_2
TB2_2A_selection_valve1,Tail Braker 2 Line 2A Selection Valve 1 State,State of selection valve 1 for Tail Braker #2 Line A.,Tail Braker 2A Hydraulic/Pneumatic System,TB2_2A_selection_valve2
TB2_2A_selection_valve2,Tail Braker 2 Line 2A Selection Valve 2 State,State of selection valve 2 for Tail Braker #2 Line A.,Tail Braker 2A Hydraulic/Pneumatic System,TB2_2A_selection_valve1
TB2_2A_SetLinearSpeed,Tail Braker 2 Line 2A Set Linear Speed,Setpoint for the linear speed of Tail Braker #2 Line A rolls.,Tail Braker 2A Control System,TB2_2A_ActualLinearSpeed; TB2_2A_SpeedRef
TB2_2A_SpeedRef,Tail Braker 2 Line 2A Speed Reference,Speed reference signal for Tail Braker #2 Line A motor drive.,Tail Braker 2A Drive Control,TB2_2A_ActualLinearSpeed; TB2_2A_SetLinearSpeed
TB2_2A_TailPos,Tail Braker 2 Line 2A Tail Position,Position of the bar's tail at Tail Braker #2 Line A.,Tail Braker 2A,TB2_2A_BarTailPosition
TB2_2A_TailSpeedSel,Tail Braker 2 Line 2A Tail Speed Selection,Selected speed for handling the tail end of the bar at Tail Braker #2 Line A.,Tail Braker 2A Control System,
TB2_2A_TorqueLimitPct,Tail Braker 2 Line 2A Torque Limit Percentage,Setpoint for the torque limit percentage of Tail Braker #2 Line A motor.,Tail Braker 2A Motor Control,TB2_2A_ActualTorquePct; TB2_2A_LimitedTorque
TB2_2B_ActualLinearSpeed,Tail Braker 2 Line 2B Actual Linear Speed,Actual linear speed of Tail Braker #2 Line B rolls.,Tail Braker 2B Drive,TB2_2B_ActualSpeed; TB2_2B_SetLinearSpeed; M003/M004 (motor); M003-B001 (encoder)
TB2_2B_ActualSpeed,Tail Braker 2 Line 2B Actual Angular Speed,Actual angular speed of Tail Braker #2 Line B motor/rolls.,Tail Braker 2B Drive,TB2_2B_ActualLinearSpeed; TB2_2B_SetLinearSpeed; M003/M004 (motor); M003-B001 (encoder)
TB2_2B_ActualTorquePct,Tail Braker 2 Line 2B Actual Torque Percentage,Actual torque percentage of Tail Braker #2 Line B motor.,Tail Braker 2B Motor,TB2_2B_LimitedTorque; TB2_2B_TorqueLimitPct
TB2_2B_BarHeadPosition,Tail Braker 2 Line 2B Bar Head Position,Position of the bar's head as it passes through Tail Braker #2 Line B.,Tail Braker 2B,TB2_2B_BarTailPosition; TB2_2B_TailPos
TB2_2B_BarTailPosition,Tail Braker 2 Line 2B Bar Tail Position,Position of the bar's tail as it passes through Tail Braker #2 Line B.,Tail Braker 2B,TB2_2B_BarHeadPosition; TB2_2B_TailPos
TB2_2B_BrakingSpeedSel,Tail Braker 2 Line 2B Braking Speed Selection,Selected braking speed for Tail Braker #2 Line B.,Tail Braker 2B Control System,
TB2_2B_HighPressClose,Tail Braker 2 Line 2B High Pressure Close Status,Status of high-pressure roll closing for Tail Braker #2 Line B.,Tail Braker 2B Roll Closing Mechanism,TB2_2B_HighPressClose_solvalve; TB2_2B_HighPressClose_solvalve_2; Y014 (command)
TB2_2B_HighPressClose_solvalve,Tail Braker 2 Line 2B High Pressure Close Solenoid Valve State,State of the solenoid valve for high-pressure roll closing on Tail Braker #2 Line B.,Tail Braker 2B Roll Closing Solenoid Valve,TB2_2B_HighPressClose; TB2_2B_HighPressClose_solvalve_2; Y014 (command)
TB2_2B_HighPressClose_solvalve_2,Tail Braker 2 Line 2B High Pressure Close Solenoid Valve 2 State,State of the second solenoid valve for high-pressure roll closing on Tail Braker #2 Line B.,Tail Braker 2B Roll Closing Solenoid Valve,TB2_2B_HighPressClose; TB2_2B_HighPressClose_solvalve; Y014 (command)
TB2_2B_HighPressureAchieveTime,Tail Braker 2 Line 2B High Pressure Achieve Time,Time taken to achieve high pressure for roll closing on Tail Braker #2 Line B.,Tail Braker 2B Roll Closing Mechanism,
TB2_2B_LimitedTorque,Tail Braker 2 Line 2B Limited Torque,Status indicating if torque limit is active for Tail Braker #2 Line B motor.,Tail Braker 2B Motor Control,TB2_2B_ActualTorquePct; TB2_2B_TorqueLimitPct
TB2_2B_MotorCurrent,Tail Braker 2 Line 2B Motor Current,Electrical current drawn by Tail Braker #2 Line B motor.,Tail Braker 2B Motor,M003/M004
TB2_2B_OverspeedSel,Tail Braker 2 Line 2B Overspeed Selection,Selected overspeed setting for Tail Braker #2 Line B.,Tail Braker 2B Control System,TB2_2B_ReducedOvspdSel
TB2_2B_ReducedOvspdSel,Tail Braker 2 Line 2B Reduced Overspeed Selection,Selected reduced overspeed setting for Tail Braker #2 Line B.,Tail Braker 2B Control System,TB2_2B_OverspeedSel
TB2_2B_RollsClose_solvalve,Tail Braker 2 Line 2B Rolls Close Solenoid Valve State,State of the solenoid valve for roll closing on Tail Braker #2 Line B.,Tail Braker 2B Roll Closing Solenoid Valve,TB2_2B_RollsCloseCmd; Y004 (command); TB2_2B_RollsClose_solvalve_2
TB2_2B_RollsClose_solvalve_2,Tail Braker 2 Line 2B Rolls Close Solenoid Valve 2 State,State of the second solenoid valve for roll closing on Tail Braker #2 Line B.,Tail Braker 2B Roll Closing Solenoid Valve,TB2_2B_RollsCloseCmd; Y004 (command); TB2_2B_RollsClose_solvalve
TB2_2B_RollsCloseCmd,Tail Braker 2 Line 2B Rolls Close Command Status,Status of the command to close rolls for Tail Braker #2 Line B.,Tail Braker 2B Control System,Y004 (command); TB2_2B_RollsClose_solvalve; TB2_2B_RollsClose_solvalve_2
TB2_2B_selection_valve1,Tail Braker 2 Line 2B Selection Valve 1 State,State of selection valve 1 for Tail Braker #2 Line B.,Tail Braker 2B Hydraulic/Pneumatic System,TB2_2B_selection_valve2
TB2_2B_selection_valve2,Tail Braker 2 Line 2B Selection Valve 2 State,State of selection valve 2 for Tail Braker #2 Line B.,Tail Braker 2B Hydraulic/Pneumatic System,TB2_2B_selection_valve1
TB2_2B_SetLinearSpeed,Tail Braker 2 Line 2B Set Linear Speed,Setpoint for the linear speed of Tail Braker #2 Line B rolls.,Tail Braker 2B Control System,TB2_2B_ActualLinearSpeed; TB2_2B_SpeedRef
TB2_2B_SpeedRef,Tail Braker 2 Line 2B Speed Reference,Speed reference signal for Tail Braker #2 Line B motor drive.,Tail Braker 2B Drive Control,TB2_2B_ActualLinearSpeed; TB2_2B_SetLinearSpeed
TB2_2B_TailPos,Tail Braker 2 Line 2B Tail Position,Position of the bar's tail at Tail Braker #2 Line B.,Tail Braker 2B,TB2_2B_BarTailPosition
TB2_2B_TailSpeedSel,Tail Braker 2 Line 2B Tail Speed Selection,Selected speed for handling the tail end of the bar at Tail Braker #2 Line B.,Tail Braker 2B Control System,
TB2_2B_TorqueLimitPct,Tail Braker 2 Line 2B Torque Limit Percentage,Setpoint for the torque limit percentage of Tail Braker #2 Line B motor.,Tail Braker 2B Motor Control,TB2_2B_ActualTorquePct; TB2_2B_LimitedTorque
TB2_Tail braker order to switch high pressure,Tail Braker 2 High Pressure Switch Order,Command signal for Tail Braker #2 to switch to high pressure mode for roll closing.,Tail Braker 2 Control System,
TB21A_ClsPressure,Tail Braker 2 Line 1A Closing Pressure,Closing pressure status/value for Tail Braker #1 Line A rolls.,Tail Braker 1A Roll Closing Mechanism,B011
TB21A_TailAfterShearOnTBLine,Tail Braker 2 Line 1A Tail After Shear on TB Line,Indicates presence of bar tail on Tail Braker #1 Line A after a shear operation.,Tail Braker 1A Bar Detection,
TB21A_WORK_DB.BrakingTriggerPoint,Tail Braker 2 Line 1A Braking Trigger Point,Calculated or set trigger point for braking on Tail Braker #1 Line A.,Tail Braker 1A Control System,
TB21A_WR_SAFETY_TIME,Tail Braker 2 Line 1A Work Roll Safety Time,Safety time parameter related to work roll operations on Tail Braker #1 Line A.,Tail Braker 1A Control System,
TB21B_ClsPressure,Tail Braker 2 Line 1B Closing Pressure,Closing pressure status/value for Tail Braker #1 Line B rolls.,Tail Braker 1B Roll Closing Mechanism,B012
TB21B_TailAfterShearOnTBLine,Tail Braker 2 Line 1B Tail After Shear on TB Line,Indicates presence of bar tail on Tail Braker #1 Line B after a shear operation.,Tail Braker 1B Bar Detection,
TB21B_WORK_DB.BrakingTriggerPoint,Tail Braker 2 Line 1B Braking Trigger Point,Calculated or set trigger point for braking on Tail Braker #1 Line B.,Tail Braker 1B Control System,
TB21B_WR_SAFETY_TIME,Tail Braker 2 Line 1B Work Roll Safety Time,Safety time parameter related to work roll operations on Tail Braker #1 Line B.,Tail Braker 1B Control System,
TB22A_ClsPressure,Tail Braker 2 Line 2A Closing Pressure,Closing pressure status/value for Tail Braker #2 Line A rolls.,Tail Braker 2A Roll Closing Mechanism,B013
TB22A_TailAfterShearOnTBLine,Tail Braker 2 Line 2A Tail After Shear on TB Line,Indicates presence of bar tail on Tail Braker #2 Line A after a shear operation.,Tail Braker 2A Bar Detection,
TB22A_WORK_DB.BrakingTriggerPoint,Tail Braker 2 Line 2A Braking Trigger Point,Calculated or set trigger point for braking on Tail Braker #2 Line A.,Tail Braker 2A Control System,
TB22A_WR_SAFETY_TIME,Tail Braker 2 Line 2A Work Roll Safety Time,Safety time parameter related to work roll operations on Tail Braker #2 Line A.,Tail Braker 2A Control System,
TB22B_ClsPressure,Tail Braker 2 Line 2B Closing Pressure,Closing pressure status/value for Tail Braker #2 Line B rolls.,Tail Braker 2B Roll Closing Mechanism,B014
TB22B_TailAfterShearOnTBLine,Tail Braker 2 Line 2B Tail After Shear on TB Line,Indicates presence of bar tail on Tail Braker #2 Line B after a shear operation.,Tail Braker 2B Bar Detection,
TB22B_WORK_DB.BrakingTriggerPoint,Tail Braker 2 Line 2B Braking Trigger Point,Calculated or set trigger point for braking on Tail Braker #2 Line B.,Tail Braker 2B Control System,
TB22B_WR_SAFETY_TIME,Tail Braker 2 Line 2B Work Roll Safety Time,Safety time parameter related to work roll operations on Tail Braker #2 Line B.,Tail Braker 2B Control System,
HMD22,Hot Metal Detector 22,Hot metal detector at a specific location (22, likely before or at cooling bed entry).,Cooling Bed Area,
HMD28_TWCA_ENTRY,Hot Metal Detector 28 Twin Channel A Entry,Hot metal detector at the entry of Twin Channel A.,Twin Channel A,HMD28_TWCA_ENTRY_FILTERED
HMD28_TWCA_ENTRY_FILTERED,Hot Metal Detector 28 Twin Channel A Entry Filtered,Filtered signal from HMD28 at the entry of Twin Channel A.,Twin Channel A,HMD28_TWCA_ENTRY
HMD29_TWCB_ENTRY,Hot Metal Detector 29 Twin Channel B Entry,Hot metal detector at the entry of Twin Channel B.,Twin Channel B,HMD29_TWCB_ENTRY_FILTERED
HMD29_TWCB_ENTRY_FILTERED,Hot Metal Detector 29 Twin Channel B Entry Filtered,Filtered signal from HMD29 at the entry of Twin Channel B.,Twin Channel B,HMD29_TWCB_ENTRY
HMD23_CVRD_ENTRY,Hot Metal Detector 23 Covered Entry,Hot metal detector at a covered entry point (location 23). Context suggests this is before the tail brakers/twin channels, possibly near a dividing shear.,Dividing Shear Area/Pre-Twin Channel,
HMD30_TWCA_ENTRY,Hot Metal Detector 30 Twin Channel A Entry,Hot metal detector at the entry of Twin Channel A (alternate or additional to HMD28).,Twin Channel A,HMD30_TWCA_ENTRY_FILTERED
HMD30_TWCA_ENTRY_FILTERED,Hot Metal Detector 30 Twin Channel A Entry Filtered,Filtered signal from HMD30 at the entry of Twin Channel A.,Twin Channel A,HMD30_TWCA_ENTRY
HMD31_TWCB_ENTRY,Hot Metal Detector 31 Twin Channel B Entry,Hot metal detector at the entry of Twin Channel B (alternate or additional to HMD29).,Twin Channel B,HMD31_TWCB_ENTRY_FILTERED
HMD31_TWCB_ENTRY_FILTERED,Hot Metal Detector 31 Twin Channel B Entry Filtered,Filtered signal from HMD31 at the entry of Twin Channel B.,Twin Channel B,HMD31_TWCB_ENTRY
</TAIL_BREAKER_SENSORS>
</TWIN_CHANNEL_AREA_INFO>


<FAILURE_MODE_INFO>

**Equipment: Twin Channel**

*   **Failure Mode 1:** Gap while operation not sufficient
    *   **Causes:** Improper movement of the assembly (`Channel Arm Assembly`).
    *   **Effect:** Gap (`Channel Cavities`) not as desired for bar passage, leading to jams.
    *   **Parts Affected:** Channel Arm Assembly, Channel Cavities, Bar.
    *   **Variables:**
        *   Generic Sensors: `BarExitDetectionStatus`, `ChannelArmPositionActual`, `ChannelArmPositionSetpoint`.
        *   Specific Tags: `TWC1A_BarOutOfTailBraker` (State), `TWC1A_ActPosition1` (Position), `TWC1A_SetPosition1` (Position).
    *   **Predicate Logic (Generic):**
        `IF (BarSuccessfullyEnteredChannel = FALSE AND AttemptedChannelMovement = TRUE) OR (ChannelArmPositionActual ≠ ChannelArmPositionSetpoint AND BarTransferInProgress = TRUE) THEN GapNotSufficientFailure`
    *   **Predicate Logic (Specific Tags):**
        `IF (TWC1A_BarOutOfTailBraker = FALSE AND (TWC1A_SetPosition1 ≠ Previous_TWC1A_SetPosition1)) OR (TWC1A_ActPosition1 ≠ TWC1A_SetPosition1 AND TWC1A_BarOutOfTailBraker = TRUE AND BarExpectedInChannel = TRUE) THEN GapNotSufficientFailure`

*   **Failure Mode 2:** Rotation mechanism not working as desired (Shaft assembly jam)
    *   **Causes:** Shaft assembly jam (`Rotating Shaft`).
    *   **Effect:** Shaft not moving, channel arm cannot discharge bar.
    *   **Parts Affected:** Rotation Mechanism, Rotating Shaft, Drive System, Bar.
    *   **Variables:**
        *   Generic Sensors: `ChannelArmPositionActual`, `ChannelArmPositionSetpoint`, `MotorTorqueActual`, `MotorSpeedActual`.
        *   Specific Tags: `TWC1A_ActPosition1` (Position), `TWC1A_SetPosition1` (Position), `TWC1A_ActualTorque1` (Torque), `TWC1A_ActualSpeed1` (Speed).
    *   **Predicate Logic (Generic):**
        `IF (ChannelArmPositionSetpoint ≠ Previous_ChannelArmPositionSetpoint AND ChannelArmPositionActual = Previous_ChannelArmPositionActual AND MotorTorqueActual > NormalOperationTorqueThreshold AND MotorSpeedActual < ExpectedSpeedForMovement) THEN ShaftJamFailure`
    *   **Predicate Logic (Specific Tags):**
        `IF (TWC1A_SetPosition1 ≠ Previous_TWC1A_SetPosition1 AND TWC1A_ActPosition1 = Previous_TWC1A_ActPosition1 AND TWC1A_ActualTorque1 > (TWC1A_TorqueLimit1 * 0.8) AND TWC1A_ActualSpeed1 < (TWC1A_SpeedReference1 * 0.1)) THEN ShaftJamFailure`

*   **Failure Mode 3:** Rotation mechanism not working as desired (Breakage of links - Central Beam)
    *   **Causes:** Breakage of the links of the mechanism (`Central Beam`).
    *   **Effect:** Eventual catastrophic pump failure (likely referring to hydraulic pump if movement is impeded and system strains), channel arm misalignment or collapse.
    *   **Parts Affected:** Structural Frame, Central Beam, Rotation Mechanism, Hydraulic Power Pack.
    *   **Variables:**
        *   Generic Sensors: `ChannelArmPositionActual`, `ChannelArmPositionSetpoint`, `HydraulicSystemPressure`, `VibrationSensor_StructuralFrame`.
        *   Specific Tags: `TWC1A_ActPosition1` (Position), `TWC1A_SetPosition1` (Position), (Hydraulic Pressure from Hydraulic Unit – not directly tagged here), (Vibration – not directly tagged).
    *   **Predicate Logic (Generic):**
        `IF (ChannelArmPositionActual significantly_deviates_from ExpectedPathFor_ChannelArmPositionSetpoint AND (HydraulicSystemPressure > HighPressureLimit OR VibrationSensor_StructuralFrame > HighVibrationLimit)) THEN StructuralLinkFailure`
    *   **Predicate Logic (Specific Tags):**
        `IF (TWC1A_ActPosition1 deviates_significantly_from ExpectedPathFor_TWC1A_SetPosition1 AND (AlertFrom_HydraulicUnit_HighPressure OR AlertFrom_VibrationSensor_StructuralFrame)) THEN StructuralLinkFailure`

*   **Failure Mode 4:** Rotation mechanism not working as desired (Bearing jam)
    *   **Causes:** Bearing jam (`Shaft Bearing`).
    *   **Effect:** No movement in the rotational mechanism.
    *   **Parts Affected:** Rotation Mechanism, Shaft Bearing, Drive System.
    *   **Variables:**
        *   Generic Sensors: `MotorTorqueActual`, `MotorSpeedActual`, `ChannelArmPositionActual`.
        *   Specific Tags: `TWC1A_ActualTorque1` (Torque), `TWC1A_ActualSpeed1` (Speed), `TWC1A_ActPosition1` (Position).
    *   **Predicate Logic (Generic):**
        `IF (CommandToMoveChannelArm = TRUE AND MotorSpeedActual < ExpectedSpeedForMovement AND MotorTorqueActual > HighTorqueThreshold_Jam AND ChannelArmPositionActual = Previous_ChannelArmPositionActual) THEN BearingJamFailure`
    *   **Predicate Logic (Specific Tags):**
        `IF (TWC1A_SetPosition1 ≠ Previous_TWC1A_SetPosition1 AND TWC1A_ActualSpeed1 < (TWC1A_SpeedReference1 * 0.1) AND TWC1A_ActualTorque1 > (TWC1A_TorqueLimit1 * 0.9) AND TWC1A_ActPosition1 = Previous_TWC1A_ActPosition1) THEN BearingJamFailure`

*   **Failure Mode 5:** Drive System Not working (Motor)
    *   **Causes:** No power supply in motor (`Motor`).
    *   **Effect:** Channel arm doesn't work.
    *   **Parts Affected:** Drive System, Motor.
    *   **Variables:**
        *   Generic Sensors: `MotorCurrentActual`, `MotorSpeedActual`, `CommandToRunMotor`.
        *   Specific Tags: `TWC1A_ActCurrent1` (Current), `TWC1A_ActualSpeed1` (Speed), `TWC1A_SpeedReference1` (Speed - implies command).
    *   **Predicate Logic (Generic):**
        `IF (CommandToRunMotor = TRUE AND MotorCurrentActual < LowCurrentThreshold_NoPower AND MotorSpeedActual = 0) THEN MotorNoPowerFailure`
    *   **Predicate Logic (Specific Tags):**
        `IF (TWC1A_SpeedReference1 > 0 AND TWC1A_ActCurrent1 < ExpectedIdleCurrent_NoLoad * 0.1 AND TWC1A_ActualSpeed1 = 0) THEN MotorNoPowerFailure`

*   **Failure Mode 6:** No pressure in hydraulic circuit (Hydraulic Pump faulty)
    *   **Causes:** Hydraulic Pump faulty (`Hydraulic power pack`).
    *   **Effect:** No pressure in the hydraulic oil circuit, channel arm cannot move.
    *   **Parts Affected:** Drive System, Hydraulic power pack.
    *   **Variables:**
        *   Generic Sensors: `HydraulicPressureActual`, `CommandToMoveChannelArm`, `ChannelArmPositionActual`.
        *   Specific Tags: (Hydraulic Pressure from Hydraulic Unit – not directly tagged here), `TWC1A_SetPosition1` (Position), `TWC1A_ActPosition1` (Position).
    *   **Predicate Logic (Generic):**
        `IF (CommandToMoveChannelArm = TRUE AND HydraulicPressureActual < MinRequiredPressure AND ChannelArmPositionActual = Previous_ChannelArmPositionActual) THEN HydraulicPumpFailure`
    *   **Predicate Logic (Specific Tags):**
        `IF (TWC1A_SetPosition1 ≠ Previous_TWC1A_SetPosition1 AND AlertFrom_HydraulicUnit_LowPressure AND TWC1A_ActPosition1 = Previous_TWC1A_ActPosition1) THEN HydraulicPumpFailure`

*   **Failure Mode 7:** No pressure in hydraulic circuit (Faulty solenoid coil)
    *   **Causes:** Faulty solenoid coil (`Solenoid Coil` within Hydraulic power pack).
    *   **Effect:** No movement in the rotational mechanism.
    *   **Parts Affected:** Drive System, Solenoid Coil, Hydraulic power pack.
    *   **Variables:**
        *   Generic Sensors: `SolenoidCommandSignal`, `HydraulicFlow_ToCylinder`, `ChannelArmPositionActual`.
        *   Specific Tags: (Command signal to solenoid - PLC internal), (Flow sensor if present - not listed), `TWC1A_ActPosition1` (Position).
    *   **Predicate Logic (Generic):**
        `IF (SolenoidCommandSignal = Energize AND (HydraulicFlow_ToCylinder = FALSE OR ChannelArmPositionActual = Previous_ChannelArmPositionActual)) THEN SolenoidCoilFailure`
    *   **Predicate Logic (Specific Tags):**
        `IF (PLC_Output_Solenoid_TwinChannel = Energize AND TWC1A_ActPosition1 = Previous_TWC1A_ActPosition1 AND Timeout_MovementExceeded) THEN SolenoidCoilFailure`

**Equipment: Tail Braker (Tags from JE11A01FRT & JE11A02FRT, assuming TB21A for general Tail Braker)**

*   **Failure Mode 8:** Pinch Roller Pressure low
    *   **Causes:** Faulty assembly of `Upper roller`.
    *   **Effect:** No or improper rotation of roller, ineffective braking.
    *   **Parts Affected:** Pinch Roller, Upper Roller, Pneumatic System.
    *   **Variables:**
        *   Generic Sensors: `PinchRollClosingPressureActual`, `PinchRollClosingPressureSetpoint`.
        *   Specific Tags: `TB21A_ClsPressure` (Pressure).
    *   **Predicate Logic (Generic):**
        `IF (PinchRollClosingPressureActual < (PinchRollClosingPressureSetpoint * 0.8) AND CommandToCloseRolls = TRUE) THEN PinchRollLowPressureFailure`
    *   **Predicate Logic (Specific Tags):**
        `IF (TB21A_ClsPressure < (Target_TB21A_ClsPressure * 0.8) AND (RollsCloseCommand = TRUE OR TB2_1A_HighPressClose = TRUE)) THEN PinchRollLowPressureFailure`

*   **Failure Mode 9:** Pinch Roller Bearing failure
    *   **Causes:** Wear, contamination, overheating, misalignment of `Roller bearings & Thrust bearing`.
    *   **Effect:** No or improper rotation of roller, increased friction, potential seizure.
    *   **Parts Affected:** Pinch Roller, Roller Bearings, Thrust Bearing, Drive Motor.
    *   **Variables:**
        *   Generic Sensors: `MotorTorqueActual`, `RollerSpeedActual`, `BearingTemperature` (if available), `Vibration_PinchRoller`.
        *   Specific Tags: `TB2_1A_ActualTorquePct` (Percent), `TB2_1A_ActualLinearSpeed` (Speed), `TB_LUB_DeliveryOilTemperature` (Temperature - indirect via lube oil), `M001-S912` (Motor Temperature Thermostat - generic).
    *   **Predicate Logic (Generic):**
        `IF (MotorTorqueActual > HighFrictionTorqueThreshold AND RollerSpeedActual < ExpectedSpeed) OR (BearingTemperature > MaxLimit OR Vibration_PinchRoller > MaxLimit) THEN PinchRollerBearingFailure`
    *   **Predicate Logic (Specific Tags):**
        `IF (TB2_1A_ActualTorquePct > (TB2_1A_TorqueLimitPct * 0.9) AND TB2_1A_ActualLinearSpeed < (TB2_1A_SetLinearSpeed * 0.5)) OR (TB_LUB_DeliveryOilTemperature > MaxOilTempLimit OR M001-S912 = Active) THEN PinchRollerBearingFailure`

*   **Failure Mode 10:** Pinch Roll damage
    *   **Causes:** Peeling or crack on `Upper roller & lower roller`.
    *   **Effect:** No or improper rotation of roller, uneven braking, bar marking.
    *   **Parts Affected:** Pinch Roller, Upper Roller, Lower Roller, Bar.
    *   **Variables:**
        *   Generic Sensors: `BarSurfaceQuality` (visual), `Vibration_PinchRoller`.
        *   Specific Tags: (Visual inspection), (Vibration sensor data - not directly listed).
    *   **Predicate Logic (Generic):**
        `IF (VisualInspection = Damage_Detected OR Vibration_PinchRoller > HighVibration_Damage) THEN PinchRollDamageFailure`
    *   **Predicate Logic (Specific Tags):**
        `IF (OperatorInput_RollDamage = TRUE OR VibrationSensor_TailBraker > Threshold) THEN PinchRollDamageFailure`

*   **Failure Mode 11:** Roller Shaft damage (No movement of roll assembly)
    *   **Causes:** Broken bolts of the coupling, `Roller shaft damage`.
    *   **Effect:** No rollers rotation.
    *   **Parts Affected:** Roller Shaft, Coupling, Pinch Roller.
    *   **Variables:**
        *   Generic Sensors: `MotorSpeedActual`, `RollerSpeedActual`.
        *   Specific Tags: `TB2_1A_ActualSpeed` (Speed - motor/system), `TB2_1A_ActualLinearSpeed` (Speed - bar/roller surface).
    *   **Predicate Logic (Generic):**
        `IF (MotorSpeedActual > 0 AND RollerSpeedActual = 0 AND CommandToRun = TRUE) THEN RollerShaftFailure_Coupling`
    *   **Predicate Logic (Specific Tags):**
        `IF (TB2_1A_ActualSpeed > 0 AND TB2_1A_ActualLinearSpeed = 0 AND TB2_1A_SetLinearSpeed > 0) THEN RollerShaftFailure_Coupling`

*   **Failure Mode 12:** Gear box - No required output speed / Jerks
    *   **Causes:** Worn out gears (`Gear assembly`), Damaged shaft (`Shaft`).
    *   **Effect:** No roller rotation or Improper roller rotation.
    *   **Parts Affected:** Gear Box, Gears, Shaft, Pinch Roller.
    *   **Variables:**
        *   Generic Sensors: `RollerSpeedActual`, `MotorTorqueActual`, `Vibration_Gearbox`.
        *   Specific Tags: `TB2_1A_ActualLinearSpeed` (Speed), `TB2_1A_ActualTorquePct` (Percent), (Vibration sensor - not listed).
    *   **Predicate Logic (Generic):**
        `IF ((RollerSpeedActual < (ExpectedSpeed * 0.8) AND MotorTorqueActual < NormalLoadTorque) OR (Vibration_Gearbox > HighVibration_GearDamage)) THEN GearboxFailure`
    *   **Predicate Logic (Specific Tags):**
        `IF ((TB2_1A_ActualLinearSpeed < (TB2_1A_SetLinearSpeed * 0.8) AND TB2_1A_ActualTorquePct < (TB2_1A_TorqueLimitPct * 0.5)) OR (VibrationSensor_TailBrakerGearbox > Threshold)) THEN GearboxFailure`

*   **Failure Mode 13:** Pneumatic System - Low air pressure / Improper stroke
    *   **Causes:** Damaged `Pneumatic cylinders seals` or `Pneumatic cylinder rod`.
    *   **Effect:** Product defective (ineffective braking).
    *   **Parts Affected:** Pneumatic System, Pneumatic Cylinder, Seals, Rod.
    *   **Variables:**
        *   Generic Sensors: `AirPressure_Inlet`, `AirPressure_Outlet`, `CylinderPositionFeedback` (if available).
        *   Specific Tags: `TB_ACC_IN_AIR_PRESSURE` (Pressure), `TB_ACC_OUT_AIR_PRESSURE` (Pressure).
    *   **Predicate Logic (Generic):**
        `IF (AirPressure_Inlet > MinSupplyPressure AND AirPressure_Outlet < MinOperatingPressure) OR (CommandToActuateCylinder = TRUE AND CylinderPositionFeedback ≠ ExpectedPosition) THEN PneumaticSystemFailure`
    *   **Predicate Logic (Specific Tags):**
        `IF (TB_ACC_IN_AIR_PRESSURE > MinSupplyPressure AND TB_ACC_OUT_AIR_PRESSURE < MinOperatingPressure) OR (TB21A_ClsPressure < RequiredPressure AND (RollsCloseCommand = TRUE OR TB2_1A_HighPressClose = TRUE)) THEN PneumaticSystemFailure`

*   **Failure Mode 14:** Braking Disc System - Roller speed not slowing down
    *   **Causes:** Worn out `Braking disc`.
    *   **Effect:** Product defective (bar not slowed sufficiently).
    *   **Parts Affected:** Braking Disc System, Braking Disc, Bar.
    *   **Variables:**
        *   Generic Sensors: `BarSpeed_AfterBraking`, `BrakingCommandActive`.
        *   Specific Tags: `TB2_1A_ActualLinearSpeed` (Speed), `TB21A_WORK_DB.BrakingTriggerPoint` (State), `TB2_1A_BRAKING CYCLE ACTIVE` (State).
    *   **Predicate Logic (Generic):**
        `IF (BrakingCommandActive = TRUE AND BarSpeed_AfterBraking > TargetExitSpeed) THEN BrakingDiscFailure`
    *   **Predicate Logic (Specific Tags):**
        `IF (TB2_1A_BRAKING CYCLE ACTIVE = TRUE AND TB21A_WORK_DB.BrakingTriggerPoint = TRUE AND TB2_1A_ActualLinearSpeed > TargetVFREN_PostBraking) THEN BrakingDiscFailure`

*   **Failure Mode 15:** Guide Roller System - Bar misalignment
    *   **Causes:** Loose assembly of `Guide rollers`.
    *   **Effect:** Product defective, potential jam.
    *   **Parts Affected:** Guide Roller System, Guide Rollers, Bar.
    *   **Variables:**
        *   Generic Sensors: `BarPosition_Lateral` (if sensed), `VisualInspection_Alignment`.
        *   Specific Tags: `TB2_1A_BarHeadPosition` (Position - primarily longitudinal, but large deviations might imply lateral issues if combined with other data or visual).
    *   **Predicate Logic (Generic):**
        `IF (VisualInspection_Alignment = Misaligned OR BarPosition_Lateral > MaxDeviation) THEN GuideRollerMisalignment`
    *   **Predicate Logic (Specific Tags):**
        `IF (OperatorInput_BarMisalignedAtTailBraker = TRUE) THEN GuideRollerMisalignment`

*   **Failure Mode 16:** Control and Monitoring - Improper braking
    *   **Causes:** Faulty `Solenoid valve`.
    *   **Effect:** Product defective (incorrect braking application).
    *   **Parts Affected:** Control and Monitoring, Solenoid Valves, Pneumatic System.
    *   **Variables:**
        *   Generic Sensors: `SolenoidCommandSignal`, `SolenoidValveFeedback` (if available), `BrakingPerformance`.
        *   Specific Tags: `TB2_1A_RollsClose_solvalve_2` (State - assuming this is a key valve for braking actuation), `TB2_1A_HighPressClose_solvalve_2` (State).
    *   **Predicate Logic (Generic):**
        `IF (SolenoidCommandSignal = Energize AND (SolenoidValveFeedback = NotEnergized OR BrakingPerformance = Poor)) THEN SolenoidBrakingFailure`
    *   **Predicate Logic (Specific Tags):**
        `IF ((RollsCloseCommand = TRUE AND TB2_1A_RollsClose_solvalve_2 = FALSE) OR (TB2_1A_HighPressClose = TRUE AND TB2_1A_HighPressClose_solvalve_2 = FALSE)) AND BrakingCyclePerformancePoor THEN SolenoidBrakingFailure`

*   **Failure Mode 17:** Cooling system - High oil temperature
    *   **Causes:** Choked `Oil cooler`, `Oil pump` not working, Choked `Oil Filter`.
    *   **Effect:** Overheating of the assembly (Tail Braker gearbox/bearings).
    *   **Parts Affected:** Cooling System, Oil Cooler, Oil Pump, Oil Filter, Lubricated Components.
    *   **Variables:**
        *   Generic Sensors: `OilTemperature_Delivery`, `OilFlowRate`, `FilterDifferentialPressure`.
        *   Specific Tags: `TB_LUB_DeliveryOilTemperature` (Temperature), `TB_LUB_BushMinFlow` (Flow - generic, assume similar for oil pump), (Filter DP sensor - not listed).
    *   **Predicate Logic (Generic):**
        `IF (OilTemperature_Delivery > MaxOilTemp) AND (OilFlowRate < MinOilFlow OR FilterDifferentialPressure > MaxDP) THEN CoolingSystemFailure_HighOilTemp`
    *   **Predicate Logic (Specific Tags):**
        `IF (TB_LUB_DeliveryOilTemperature > MaxAllowableOilTemp) AND (TB_LUB_BushMinFlow = Low OR OilFilterDP_TailBraker > MaxDP) THEN CoolingSystemFailure_HighOilTemp`

*   **Failure Mode 18:** Driver - No rotation of rollers
    *   **Causes:** `Motor` faulty (e.g., winding).
    *   **Effect:** No motion to roller assembly.
    *   **Parts Affected:** Driver, Motor, Pinch Roller.
    *   **Variables:**
        *   Generic Sensors: `MotorCurrentActual`, `MotorSpeedActual`, `CommandToRunMotor`.
        *   Specific Tags: `TB2_1A_MotorCurrent` (Current), `TB2_1A_ActualSpeed` (Speed), `TB2_1A_SetLinearSpeed` (Speed - implies command).
    *   **Predicate Logic (Generic):**
        `IF (CommandToRunMotor = TRUE AND MotorSpeedActual = 0 AND MotorCurrentActual > NormalStartCurrentButNoRotation) THEN MotorFaultFailure`
    *   **Predicate Logic (Specific Tags):**
        `IF (TB2_1A_SetLinearSpeed > 0 AND TB2_1A_ActualSpeed = 0 AND TB2_1A_MotorCurrent > ExpectedStartCurrent_NoRotation) THEN MotorFaultFailure`


This section provides information about failures in the form of a table. Each row contains following information

-Failure Mode : name of failure mode,
-Description : description of failure mode,
-Component: component involved in the failure mode,
-Sub-component : any sub-components associated with the failure mode,
-Probable Cause : causes of the failure mode,
-Effects: effect,
-Prevention Method: for fixing the problem. it will be marked as 'none' if there are no recommendations.
-Recommended Actions: for fixing the problem. it will be marked as 'none' if there are no recommendations.
-Symptoms: symptoms of the failure mode,
-Variables: variables that can be used to detect the failure mode,
-Generic Sensors: generic sensors that can be used to detect the failure mode,
-Specific Sensors: specific tags that can be used to detect the failure mode.
-Sensor Trends: sensor trends that can be used to detect the failure mode.

-FAILURE MODE TABLE DATA

"Failure Mode","Description","Components","Sub-components","Probable Cause","Effects","Prevention Method","Recommended Actions","Symptoms","Variables","Generic Sensors","Specific Sensors","Sensor Trends"
"Tail Braker Drive System Failure","The tail braker's drive system fails, resulting in the inability to properly pull the bar from the upstream shear or apply the necessary braking torque.","Tail Braker Assembly","Drive Motor","DC Motor electrical fault (winding short/open)","Tail braker cannot pull/brake the bar. Bar enters twin channel at incorrect speed. Potential jams. Production stoppage.","Implement predictive maintenance for motor (vibration, thermal imaging, electrical tests). Ensure proper cooling.","Motor not running/erratic. Unusual noises. Overheating. Drive controller faults. No/inconsistent bar movement. Tripped protections.","Drive Status, Motor Speed, Motor Torque/Current, Motor Winding Temperature, Klixon Status, Overspeed Switch Status","Motor Speed Sensor, Motor Current/Torque Sensor, Temperature Sensors, Power Supply Monitor","M00x (via Drive Status), TB2_1A_ActualSpeed, TB2_1A_MotorCurrent, TB2_1A_ActualTorquePct, M00x-S912, M00x-S902/S903, M00x-S904/S905, M00x-S901","Motor speed lower than setpoint/zero. Current high (stall) or low (no power). Temperature rising. Klixon/overspeed active."
"Tail Braker Drive System Failure","The tail braker's drive system fails, resulting in the inability to properly pull the bar from the upstream shear or apply the necessary braking torque.","Tail Braker Assembly","Drive Motor","DC Motor mechanical fault (bearing seizure)","Tail braker cannot pull/brake the bar. Bar enters twin channel at incorrect speed. Potential jams. Production stoppage.","Implement predictive maintenance for motor (vibration analysis). Ensure proper lubrication if applicable to motor bearings.","Motor seized, humming sound, high current. Unusual noises prior to failure. Overheating. Drive controller faults.","Drive Status, Motor Speed, Motor Torque/Current, Motor Winding Temperature","Motor Speed Sensor, Motor Current/Torque Sensor, Temperature Sensors, Vibration Sensor","M00x (via Drive Status), TB2_1A_ActualSpeed, TB2_1A_MotorCurrent, TB2_1A_ActualTorquePct, M00x-S912","Motor speed zero. Current very high (stall). Temperature rising. High vibration prior to seizure."
"Tail Braker Drive System Failure","The tail braker's drive system fails, resulting in the inability to properly pull the bar from the upstream shear or apply the necessary braking torque.","Tail Braker Assembly","Drive Controller","DC Drive controller malfunction.","Tail braker cannot pull/brake the bar. Incorrect speed/torque control. Potential jams. Production stoppage.","Ensure robust power supply and controller health checks. Regular diagnostic checks. Maintain controlled environment for electronics.","Drive controller fault alarms. Erratic motor behavior. No motor response.","Drive Status, Controller Fault Codes, Motor Speed, Motor Torque","Drive Controller Diagnostics","Drive Status (Fault reported by controller)","Controller fault codes active. Motor behavior inconsistent with commands."
"Tail Braker Drive System Failure","The tail braker's drive system fails, resulting in the inability to properly pull the bar from the upstream shear or apply the necessary braking torque.","Tail Braker Assembly","Power Supply","Loss of power to drive motor or controller.","Tail braker cannot pull/brake the bar. Complete loss of function. Production stoppage.","Ensure robust power supply, check connections, use UPS for control circuits if critical.","Motor and controller inactive. No fault codes if complete power loss to controller. HMI shows no communication.","Power Supply Voltage, Drive Status","Power Supply Monitor","(No specific tag for drive power input; inferred from general electrical system health)","Zero voltage at drive input. Drive status inactive."
"Tail Braker Drive System Failure","The tail braker's drive system fails, resulting in the inability to properly pull the bar from the upstream shear or apply the necessary braking torque.","Tail Braker Assembly","Drive Motor","Motor overheating (thermostat trip or Klixon activation).","Tail braker drive disabled by protection. Inability to pull/brake bar.","Ensure motor cooling system is effective (see Motor Cooling Failure). Check Klixon settings and functionality. Investigate root cause of overheating.","Motor temperature alarm/trip. Klixon status active. Motor stops.","Motor Winding Temperature, Klixon Status","Temperature Sensors, Klixon Switches","M00x-S912, M00x-S902/S903, M00x-S904/S905","Temperature exceeds threshold. Klixon switch changes state."
"Tail Braker Drive System Failure","The tail braker's drive system fails, resulting in the inability to properly pull the bar from the upstream shear or apply the necessary braking torque.","Tail Braker Assembly","Drive Motor","Armature/field fault (Klixon activation).","Tail braker drive disabled by protection. Inability to pull/brake bar.","Investigate cause of armature/field fault (e.g., high current, insulation breakdown). Check motor condition.","Klixon status active for armature/field. Motor may stop or run erratically. Drive fault.","Klixon Status (Armature/Field), Motor Current","Klixon Switches","M00x-S902/S903 (Armature), M00x-S904/S905 (Field)","Specific Klixon for armature or field changes state."
"Tail Braker Drive System Failure","The tail braker's drive system fails, resulting in the inability to properly pull the bar from the upstream shear or apply the necessary braking torque.","Tail Braker Assembly","Drive Motor","Overspeed switch trip.","Tail braker drive disabled by protection. Inability to pull/brake bar (if stop due to overspeed).","Investigate cause of overspeed (e.g., controller malfunction, encoder issue, mechanical problem). Check overspeed switch functionality.","Overspeed alarm/trip. Motor stops abruptly.","Overspeed Switch Status, Motor Speed","Overspeed Switch","M00x-S901","Overspeed switch changes state. Motor speed may have spiked before trip."
"Tail Braker Drive System Failure","The tail braker's drive system fails, resulting in the inability to properly pull the bar from the upstream shear or apply the necessary braking torque.","Tail Braker Assembly","Gearbox","Internal failure (worn/broken gears, bearing failure).","No/improper torque transmission from motor to rolls. Tail braker cannot pull/brake bar.","Predictive maintenance (vibration analysis, oil analysis). Ensure proper lubrication.","Unusual noises (grinding, whining), overheating, vibration, oil leaks, motor runs but rolls don't.","Gearbox Temperature, Vibration, Oil Condition","Temperature Sensor (Gearbox Oil), Vibration Sensor, Oil Level/Condition Sensor","TB_LUB_DeliveryOilTemperature","Gearbox temperature rising. High vibration. Abnormal oil analysis results."
"Tail Braker Drive System Failure","The tail braker's drive system fails, resulting in the inability to properly pull the bar from the upstream shear or apply the necessary braking torque.","Tail Braker Assembly","Gearbox","Lubrication failure (see Lubrication Failure mode).","Increased friction, wear, leading to gearbox internal failure. Tail braker cannot pull/brake bar.","Ensure robust lubrication system (see Lubrication Failure mode).","Symptoms of lubrication failure (low flow/pressure, high oil temp), followed by gearbox symptoms (noise, vibration, heat).","Oil Flow, Oil Pressure, Oil Temperature, Gearbox Temperature, Vibration","Flow Switch, Pressure Switch, Temperature Sensor","S051, S052 (pinion lube), S011, S012 (pinion pressure), S151-S154 (bearing lube flow), S111-S114 (bearing lube pressure), TB_LUB_DeliveryOilTemperature","Low oil flow/pressure, high oil temperature, leading to gearbox temperature rise and vibration."
"Tail Braker Drive System Failure","The tail braker's drive system fails, resulting in the inability to properly pull the bar from the upstream shear or apply the necessary braking torque.","Tail Braker Assembly","Coupling","Mechanical failure of coupling elements between motor and gearbox.","Loss of power transmission between motor and gearbox. Tail braker cannot pull/brake bar.","Regular inspection of coupling integrity and bolt tightness. Ensure proper alignment.","Motor runs but gearbox input shaft/rolls don't, unusual noise at coupling, visible damage.","Motor Speed, Gearbox Input Speed","Speed Sensors (on either side of coupling if available), Visual Inspection","TB2_1A_ActualSpeed (motor), (Gearbox input speed not directly tagged)","Motor speed normal, but gearbox input or roll speed is zero/low."
"Tail Braker Drive System Failure","The tail braker's drive system fails, resulting in the inability to properly pull the bar from the upstream shear or apply the necessary braking torque.","Tail Braker Assembly","Coupling","Broken bolts of the coupling (roller shaft to gearbox or motor to gearbox).","Loss of power transmission. No rollers rotation.","Regular inspection and torque checks of coupling bolts. Use appropriate grade bolts and locking mechanisms.","Motor runs but no movement in subsequent component (gearbox/rolls), sudden unusual noise/jolt at coupling, visible loose/broken bolts.","Motor Speed, Roll Speed","Speed Sensors, Visual Inspection","TB2_1A_ActualSpeed, TB2_1A_ActualLinearSpeed","Motor speed normal, but roll speed is zero/low."
"Tail Braker Drive System Failure","The tail braker's drive system fails, resulting in the inability to properly pull the bar from the upstream shear or apply the necessary braking torque.","Tail Braker Assembly","Encoder","Malfunction (loss of signal, incorrect readings), mechanical damage, cabling issue.","Incorrect speed/position feedback to drive controller, leading to improper motor control. Tail braker cannot pull/brake bar correctly.","Regular inspection of encoder, cabling, and mounting. Protect from physical damage and contamination. Perform regular calibration/checks if possible.","Drive controller fault alarms related to encoder. Erratic motor behavior. Incorrect bar speed control.","Encoder Signal Quality/Counts, Drive Fault Codes","Encoder Feedback Signal","M00x-B001","Erratic or missing encoder feedback. Drive faults indicating encoder issues."
"Tail Braker Roll Closing Failure","The pinch rolls of the tail braker fail to close onto the bar with the required pressure, or fail to close at all.","Tail Braker Assembly","Upper Roller","Faulty assembly of upper roller.","Rolls do not close or apply inadequate pressure. Pinch Roller Pressure low.","Ensure correct assembly procedures are followed. Verify component integrity before assembly.","Low closing pressure alarm. Visible misalignment or improper movement of upper roller. Ineffective braking.","Pinch Roll Closing Pressure, Roller Position","Pressure Sensor, Position Sensor (if available)","TB21A_ClsPressure","Closing pressure (TB21A_ClsPressure) below setpoint (Target_TB21A_ClsPressure * 0.8) when close command active."
"Tail Braker Roll Closing Failure","The pinch rolls of the tail braker fail to close onto the bar with the required pressure, or fail to close at all.","Tail Braker Assembly","Pneumatic Cylinder","Internal leaks or damaged seals in pneumatic cylinder.","Cylinder fails to extend/retract or apply sufficient force. Rolls do not close or apply inadequate pressure. Product defective.","Regular inspection and maintenance of pneumatic cylinders. Check for air leaks. Replace seals as per schedule or on condition.","Hissing air leaks from cylinder. Slow or incomplete cylinder movement. Low closing pressure.","Cylinder Position (if sensed), Closing Pressure, Air Consumption Rate","Position Sensor (Cylinder), Pressure Sensor (Cylinder Outlet/Supply)","TB21A_ClsPressure, TB_ACC_IN_AIR_PRESSURE, TB_ACC_OUT_AIR_PRESSURE","TB21A_ClsPressure < RequiredPressure. High air consumption if leaking."
"Tail Braker Roll Closing Failure","The pinch rolls of the tail braker fail to close onto the bar with the required pressure, or fail to close at all.","Tail Braker Assembly","Pneumatic Cylinder","Bent rod or mechanical seizure of pneumatic cylinder.","Cylinder movement impeded or blocked. Rolls do not close or open.","Protect cylinder rod from impact. Ensure alignment. Lubricate rod if specified.","Visible damage to rod. Cylinder stuck. Rolls unresponsive to command. Motor driving cylinder may stall or show high current (if applicable to control logic).","Cylinder Position (if sensed), Motor Current (if cylinder is motor-driven, not typical for simple pneumatics)","Position Sensor (Cylinder)","(No specific tag for cylinder position)","Rolls do not move despite command. Cylinder physically stuck."
"Tail Braker Roll Closing Failure","The pinch rolls of the tail braker fail to close onto the bar with the required pressure, or fail to close at all.","Tail Braker Assembly","Pneumatic Control Valves (Y001-Y004)","Solenoid coil failure (burnout, open circuit).","Valve fails to shift, preventing air flow to cylinder. Rolls do not close or open.","Regular testing of solenoid valve operation. Check electrical connections and coil resistance.","Solenoid does not click when energized/de-energized. Rolls unresponsive to command.","Solenoid Command Signal, Valve State Feedback (if available)","Solenoid Valve Status Indicator (Electrical)","Y001, Y002, Y003, Y004","No voltage/current at solenoid when commanded, or valve does not shift (no sound/feedback)."
"Tail Braker Roll Closing Failure","The pinch rolls of the tail braker fail to close onto the bar with the required pressure, or fail to close at all.","Tail Braker Assembly","Pneumatic Control Valves (Y001-Y004)","Valve sticking or internal leaks.","Valve does not shift correctly or leaks air, leading to slow/incomplete actuation or inability to hold pressure. Rolls may close slowly or with low force.","Ensure clean air supply. Use appropriate lubrication if specified for valve type. Inspect for external leaks.","Hissing air from valve. Sluggish cylinder movement. Low closing pressure.","Air Flow, Closing Pressure, Cylinder Actuation Speed","Flow Sensor (Downstream of Valve), Pressure Sensor","TB2_1A_RollsClose_solvalve_2, TB2_1A_HighPressClose_solvalve_2 (examples)","Valve appears to energize but cylinder movement is slow/weak. Pressure does not build or hold."
"Tail Braker Roll Closing Failure","The pinch rolls of the tail braker fail to close onto the bar with the required pressure, or fail to close at all.","Tail Braker Assembly","Compressed Air System","Low system air pressure.","Insufficient air pressure to actuate pneumatic cylinders effectively. Rolls close slowly, with low force, or not at all.","Regular maintenance of compressed air system. Ensure main compressor maintains system pressure. Check for major leaks upstream.","Low air pressure reading on system gauges. Sluggish pneumatic actuation across multiple devices.","System Air Pressure","Pressure Switch/Sensor (Main Air Line or local to Tail Braker)","TB_ACC_IN_AIR_PRESSURE, TB_ACC_OUT_AIR_PRESSURE","TB_ACC_IN_AIR_PRESSURE or TB_ACC_OUT_AIR_PRESSURE below minimum required levels."
"Tail Braker Roll Closing Failure","The pinch rolls of the tail braker fail to close onto the bar with the required pressure, or fail to close at all.","Tail Braker Assembly","Compressed Air System","Leaks in air lines to tail braker cylinders/valves.","Loss of air pressure at the point of use. Rolls close slowly, with low force, or not at all.","Regular inspection of air lines and fittings for leaks (e.g., soap bubble test).","Audible hissing of air near tail braker. Low closing force despite adequate system pressure further upstream.","Local Air Pressure (if measured), Cylinder Actuation Speed/Force","(Local pressure sensor if available)","TB_ACC_OUT_AIR_PRESSURE (if local enough)","Pressure drop between system and actuator. Slow actuation."
"Tail Braker High-Pressure Braking Failure","The tail braker fails to apply or sustain the increased high-pressure clamping force required during the final stage of braking.","Tail Braker Assembly","High-Pressure Solenoid Valves (Y011-Y014)","Failure of high-pressure solenoid valve (coil burnout, sticking).","Valve fails to shift to allow high-pressure air to cylinder. Insufficient final braking force. Bar exits faster than VFREN.","Regular testing of high-pressure solenoid valve operation. Check electrical connections to coils. Ensure clean air supply.","High-pressure solenoid does not actuate when commanded. Bar exit speed higher than target VFREN.","Solenoid Command (High Pressure), Valve State Feedback (High Pressure), Bar Exit Speed","Solenoid Valve Status Indicator, Speed Sensor","Y011, Y012, Y013, Y014, TB2_1A_HighPressClose_solvalve_2 (examples), TB2_1A_ActualLinearSpeed","High-pressure solenoid valve feedback (if available) shows no change despite command. TB2_1A_ActualLinearSpeed > TargetVFREN when high pressure braking expected."
"Tail Braker High-Pressure Braking Failure","The tail braker fails to apply or sustain the increased high-pressure clamping force required during the final stage of braking.","Tail Braker Assembly","Compressed Air System","Low compressed air pressure available for the high-pressure stage.","Insufficient air pressure to achieve the required high clamping force. Bar exits faster than VFREN.","Ensure dedicated high-pressure air supply (if separate) is functional and regulators are set correctly. Check for leaks in HP lines.","Low pressure reading on high-pressure circuit gauge (if present). Bar exit speed higher than target VFREN.","High-Pressure Circuit Air Pressure, Bar Exit Speed","Pressure Sensor (High-Pressure Circuit)","TB_ACC_IN_AIR_PRESSURE (if it supplies HP stage too), TB2_1A_ActualLinearSpeed","Air pressure in HP circuit below required minimum. TB2_1A_ActualLinearSpeed > TargetVFREN when high pressure braking expected."
"Tail Braker Lubrication System Failure","Inadequate lubrication to the tail braker's gearbox or bearings.","Tail Braker Assembly","Oil Cooler (within Lubrication Unit JE11Y10CLC)","Choked or fouled oil cooler.","Reduced cooling efficiency of lubricating oil. Oil temperature rises, leading to overheating of tail braker components.","Regular cleaning of oil cooler. Monitor oil temperature and differential pressure across cooler if available.","High oil temperature alarms (delivery oil). Reduced heat dissipation.","Oil Temperature (Delivery), Oil Flow Rate","Temperature Sensor, Flow Sensor","TB_LUB_DeliveryOilTemperature","TB_LUB_DeliveryOilTemperature rises above normal operating range."
"Tail Braker Lubrication System Failure","Inadequate lubrication to the tail braker's gearbox or bearings.","Tail Braker Assembly","Oil Pump (within Lubrication Unit JE11Y10CLC)","Oil pump motor failure or internal pump wear.","Reduced or no oil flow/pressure to tail braker components. Overheating and wear.","Regular maintenance of lubrication unit pumps (check motor, listen for abnormal noise, check for leaks). Monitor pump performance.","Low oil flow/pressure alarms from JE11Y10CLC. Lubrication unit fault. Pump motor not running or noisy.","Pump Motor Status, Oil Flow, Oil Pressure (from Lube Unit)","Motor Current Sensor, Flow Switch, Pressure Switch (on Lube Unit)","Alerts from JE11Y10CLC system for S051,S052,S011,S012,S151-S154,S111-S114","Low flow (S051/S052/S15x) or low pressure (S011/S012/S11x) signals from lubrication unit."
"Tail Braker Lubrication System Failure","Inadequate lubrication to the tail braker's gearbox or bearings.","Tail Braker Assembly","Oil Filter (within Lubrication Unit JE11Y10CLC)","Clogged oil filter element.","Reduced oil flow to tail braker components due to high resistance. Overheating and wear.","Regular replacement of oil filter elements based on schedule or differential pressure indication from the lubrication unit.","High differential pressure across filter alarm from JE11Y10CLC. Low oil flow downstream of filter if measured locally at tail braker.","Filter Differential Pressure (from Lube Unit), Oil Flow","Differential Pressure Switch/Sensor (on Lube Unit)","Alerts from JE11Y10CLC","Lubrication unit signals filter clogged."
"Tail Braker Motor Cooling Failure","The drive motor of the tail braker overheats due to a failure in its cooling system.","Tail Braker Assembly","Motor Cooling Water System","Low cooling water flow to motor.","Reduced cooling efficiency. Motor overheats.","Ensure cooling water supply is adequate. Check for blockages or kinks in lines. Verify cooling water pump operation.","Motor temperature high alarm. Low flow indication on cooling water circuit.","Cooling Water Flow, Motor Temperature","Flow Switch, Thermostat","M00x-S914, M00x-S912","M00x-S914 indicates low flow. M00x-S912 indicates high temperature."
"Tail Braker Motor Cooling Failure","The drive motor of the tail braker overheats due to a failure in its cooling system.","Tail Braker Assembly","Motor Cooling Water System","Cooling water filter clogged.","Reduced cooling water flow to motor. Reduced cooling efficiency. Motor overheats.","Regular cleaning or replacement of cooling water filters.","Motor temperature high alarm. Low flow indication on cooling water circuit. High differential pressure across filter if monitored.","Cooling Water Filter Status, Motor Temperature","Differential Pressure Switch (Filter), Thermostat","M00x-S913, M00x-S912","M00x-S913 indicates filter clogged. M00x-S912 indicates high temperature."
"Tail Braker Motor Cooling Failure","The drive motor of the tail braker overheats due to a failure in its cooling system.","Tail Braker Assembly","Motor Air Cooling System","Air filter clogged for motor cooling fan.","Reduced air flow for motor cooling. Reduced cooling efficiency. Motor overheats.","Regular cleaning or replacement of motor air filters.","Motor temperature high alarm. Visible dirt/blockage on air filter.","Motor Air Filter Status, Motor Temperature","Visual Inspection, Thermostat","M00x-S917, M00x-S912","M00x-S917 indicates air filter clogged. M00x-S912 indicates high temperature."
"Pinch Roller Bearing Failure","Bearings supporting the pinch rollers fail.","Tail Braker Assembly","Roller Bearings & Thrust Bearing","Wear, contamination, overheating, misalignment, lack of lubrication.","No or improper rotation of roller, increased friction, potential seizure, unusual noise, vibration.","Ensure proper lubrication from central system (JE11Y10CLC). Regular inspection for signs of wear, noise, or vibration. Check alignment.","Unusual noise (grinding, whining). Increased motor torque/current. Roller seizure or rough rotation. Overheating (indirectly via oil temp).","Motor Torque/Current, Roller Speed, Bearing Temperature (indirect), Vibration","Torque/Current Sensor, Speed Sensor, Temperature Sensor (Lube Oil), Vibration Sensor","TB2_1A_ActualTorquePct, TB2_1A_ActualLinearSpeed, TB_LUB_DeliveryOilTemperature, M00x-S912 (motor temp as indirect sign of overload)","TB2_1A_ActualTorquePct high. TB2_1A_ActualLinearSpeed low or erratic. TB_LUB_DeliveryOilTemperature high. M00x-S912 high."
"Pinch Roll Physical Damage","The surface of the upper or lower pinch roller is damaged (peeling, crack).","Tail Braker Assembly","Upper Roller / Lower Roller","Normal wear and tear, impact from bar, material defects in roller.","Uneven braking, marking of the bar surface, vibrations, potential for further roller degradation.","Regular visual inspection of roller surfaces. Monitor bar surface quality. Schedule roller refurbishment/replacement based on wear.","Visible damage (peeling, cracks) on roller surface. Marks transferred to the rolled bar. Increased vibration during operation.","Bar Surface Quality, Vibration Level, Roller Surface Condition","Visual Inspection, Vibration Sensor","(OperatorInput_RollDamage), (Vibration sensor data - not listed)","Operator reports damage or marks on bar. Increased vibration levels."
"Braking Disc System Failure","The braking disc system is unable to slow the roller speed effectively.","Tail Braker Assembly","Braking Disc","Worn out braking disc.","Reduced braking effectiveness. Bar not slowed sufficiently (VFREN not achieved). Product defective.","Regular inspection of braking disc thickness and surface condition. Replace when worn to limits.","Bar exits tail braker at a speed higher than the target VFREN. Longer than usual time to slow down. Fading brake performance.","Bar Exit Speed, Braking Time","Speed Sensor","TB2_1A_ActualLinearSpeed, TB21A_WORK_DB.BrakingTriggerPoint, TB2_1A_BRAKING CYCLE ACTIVE","TB2_1A_ActualLinearSpeed > TargetVFREN after braking trigger point and during active braking cycle."
"Guide Roller System Misalignment","Guide rollers are loose or misaligned, affecting bar travel.","Tail Braker Assembly","Guide Rollers","Loose assembly of guide rollers, worn mounting points, impact damage.","Bar misalignment through the tail braker. Potential for bar jams, scratches on bar surface, or uneven entry into twin channel.","Regular inspection of guide roller alignment and tightness of fasteners. Check for wear in guide roller bearings or pivots.","Visible bar skewing or misalignment as it passes through tail braker. Scraping sounds. Bar jams at entry/exit.","Bar Path Alignment, Audible Noise","Visual Inspection, Listening for abnormal sounds","(OperatorInput_BarMisalignedAtTailBraker)","Operator reports of bar misalignment or jams related to tail braker guides."
"Tail Braker Control System Failure (Improper Braking)","Solenoid valve controlling braking actuation is faulty.","Tail Braker Assembly","Solenoid Valve (for braking control)","Faulty solenoid coil, sticking valve mechanism.","Incorrect application or release of braking force. Product defective due to improper braking.","Regular testing of solenoid valve functionality. Ensure clean operating medium (air/hydraulic). Check electrical connections.","Braking cycle performance poor (e.g., too slow/fast braking, inconsistent braking). Solenoid does not actuate when commanded.","Solenoid Command Signal, Braking Performance Metrics (e.g., deceleration rate)","Solenoid Valve Status (if available), Bar Speed Profile","TB2_1A_RollsClose_solvalve_2, TB2_1A_HighPressClose_solvalve_2 (related to pressure application)","Command to valve sent, but pressure/braking effect not as expected. Bar speed profile during braking is abnormal."
"Twin Channel Drive System Failure","The drive system for the twin channel fails, preventing rotation of the channel arms for bar discharge.","Twin Channel Assembly","Drive Motors (M001-M008)","Electrical fault (winding), mechanical fault (bearing), overheating (thermostat, Klixons).","Channel cannot rotate. Bar remains in channel, blocking subsequent bars. Production stoppage.","Predictive maintenance (vibration, thermal imaging, electrical tests). Ensure proper motor cooling and lubrication if applicable.","Motor not running/erratic. Unusual noises. Overheating. Drive faults. Motors M001-M008 show fault status.","Motor Status, Motor Speed, Motor Torque/Current, Motor Temperature, Klixon Status","Motor Speed Sensor, Current/Torque Sensor, Temperature Sensors","M00x-S912 (Thermostat), M00x-S902/S903 (Armature Klixon), M00x-S904/S905 (Field Klixon) - Note: These specific Klixon tags are from Tail Braker, assume similar protection for Twin Channel motors or general drive fault signal","Motor speed zero/low despite command. Current high (stall) or low (no power). Temperature rising. Klixon/thermostat active."
"Twin Channel Drive System Failure","The drive system for the twin channel fails, preventing rotation of the channel arms for bar discharge.","Twin Channel Assembly","Gearboxes (associated with M001-M008)","Internal failure (worn/broken gears, bearing failure), lubrication failure.","No/improper torque transmission from motor to channel rotation mechanism. Channel cannot rotate.","Predictive maintenance (vibration analysis, oil analysis). Ensure proper lubrication (via JE11Y10CLC).","Unusual noises (grinding, whining), overheating, vibration, oil leaks. Motor runs but channel doesn't rotate or rotates erratically.","Gearbox Temperature, Vibration, Oil Condition","Temperature Sensor, Vibration Sensor, Oil Sensor","(Lubrication status via JE11Y10CLC)","Gearbox temperature rising (if monitored locally). High vibration. Alarms from shared lubrication unit."
"Twin Channel Drive System Failure","The drive system for the twin channel fails, preventing rotation of the channel arms for bar discharge.","Twin Channel Assembly","Brakes (Mxxx-Y001 for each motor group)","Brake mechanically stuck engaged, or control failure (valve) keeps brake applied.","Channel mechanically locked by brake, cannot rotate even if motor tries to drive.","Regular inspection and testing of brake system. Ensure control signals to brake release valves are correct and valves function.","Channel does not move. Motor may show high torque/current if trying to overcome an engaged brake. Brake status indicator (if any).","Brake Status, Motor Torque/Current","Brake Position Sensor (if available), Motor Current Sensor","M00x-Y001 (Brake command)","Brake release command sent (Y001 de-energized for release, if spring-applied/fail-safe), but channel does not move and motor torque is high."
"Twin Channel Drive System Failure","The drive system for the twin channel fails, preventing rotation of the channel arms for bar discharge.","Twin Channel Assembly","Encoders (B001, B008 implied for positioning)","Malfunction (loss of signal, incorrect readings), mechanical damage, cabling issue.","Incorrect position feedback to drive controller or PLC. Drive may fault, or channel rotates erratically or to wrong position.","Regular inspection of encoders, cabling, and mounting. Protect from physical damage. Perform calibration/checks.","Drive controller fault alarms (encoder-related). Erratic channel movement. Channel stops at incorrect angular positions.","Encoder Signal Quality/Counts, Drive Fault Codes, Channel Position","Position Encoder","B001, B008 (if these are the primary position encoders for the channels)","Erratic or missing encoder feedback (B001/B008). Drive faults. TWC1A_ActPosition1 not matching expected values."
"Twin Channel Rotational Mechanism Jam (Shaft/Bearing)","The main rotating shaft or its bearings for the twin channel jam, preventing rotation.","Twin Channel Assembly","Rotating Shaft / Shaft Bearings","Shaft seizure, bearing failure (wear, contamination, lack of lubrication).","Channel cannot rotate. High torque on drive motor if it attempts to move. Production stoppage.","Ensure proper lubrication of bearings (via JE11Y10CLC). Regular inspection for noise, vibration, temperature.","Loud unusual noises (grinding, screeching). Channel fails to rotate. Drive motor shows very high torque/current and may trip.","Motor Torque/Current, Channel Rotation Speed, Vibration, Temperature","Torque/Current Sensor, Speed Sensor, Vibration Sensor, Temperature Sensor","TWC1A_ActualTorque1, TWC1A_ActualSpeed1, (Lubrication via JE11Y10CLC)","TWC1A_ActualTorque1 very high (> TWC1A_TorqueLimit1 * 0.9). TWC1A_ActualSpeed1 near zero despite command. High vibration."
"Twin Channel Structural Failure (Central Beam/Links)","Breakage or critical deformation of the central beam or linkages supporting the channel arms.","Twin Channel Assembly","Central Beam, Linkages","Material fatigue, weld failure, overload due to severe jam or collision.","Loss of structural integrity. Channel arms misaligned, may collapse or jam. Potential for further catastrophic damage.","Regular structural inspections (visual, NDT if warranted). Ensure overload protections for channel movement are effective. Prevent severe jams.","Sudden loud noise. Visible deformation or collapse of channel structure. Severe channel arm misalignment. Inability to rotate.","Structural Integrity, Channel Arm Position, Vibration","Visual Inspection, Position Sensor, Vibration Sensor","TWC1A_ActPosition1, (Vibration sensor if installed)","TWC1A_ActPosition1 shows gross deviation or no movement. High, sudden vibration. Visible structural damage."
"Twin Channel Incorrect Positioning / Gap Insufficiency","Twin channel fails to achieve/maintain correct angular position for bar discharge, or channel arms fail to create sufficient gap for bar entry.","Twin Channel Assembly","Channel Arm Assembly / Rotating Shaft / Encoder System","Improper movement of channel arm assembly. Mechanical slip in rotating shaft/couplings. Encoder error (B001/B008). Drive control error. PLC logic error.","Gap in channel cavities not as desired for bar passage, leading to jams. Bar discharged incorrectly on cooling bed. Channel not at correct rest position.","Regular calibration of position feedback (B001/B008). Inspect mechanical drive train for looseness/slip. Verify PLC logic for positioning.","Bar jams at twin channel entry or exit. Incorrect bar placement on cooling bed. Channel overshoots/undershoots target position.","ChannelArmPositionActual, ChannelArmPositionSetpoint, BarExitDetectionStatus (at Tail Braker), MotorTorqueActual","Position Encoder, HMD (indirectly), Torque Sensor","TWC1A_ActPosition1, TWC1A_SetPosition1, TWC1A_BarOutOfTailBraker, TWC1A_ActualTorque1","TWC1A_ActPosition1 ≠ TWC1A_SetPosition1 when movement complete. TWC1A_BarOutOfTailBraker = FALSE when bar should have entered. Torque spikes if jamming."
"Twin Channel Hydraulic System Failure (Support Tilt)","Failure of the hydraulic system responsible for tilting the twin channel support structure (JE11A01SUP).","Twin Channel Assembly","Hydraulic Cylinders (for JE11A01SUP), Hydraulic Power Pack (JE11X10CLO)","Hydraulic pump faulty (JE11X10CLO). Faulty solenoid coil for support tilt. Cylinder leaks/failure.","Twin channel support structure cannot be tilted or held in the correct position for V-stand operations or maintenance.","Regular maintenance of hydraulic unit JE11X10CLO. Inspect cylinders for leaks. Test solenoid valves.","Support structure fails to move when commanded. Drifts from position. Low hydraulic pressure alarm from JE11X10CLO.","HydraulicPressureActual (from JE11X10CLO), SupportStructurePosition (if sensed)","Pressure Sensor (on JE11X10CLO), Position Sensor (on support structure - if available)","Alerts from JE11X10CLO (low pressure / fault)","Support structure not in desired position. Hydraulic unit JE11X10CLO alarms."
"Twin Channel False Cobble Detection at Exit","HMD at twin channel exit (B101/B102) incorrectly signals a cobble (bar present when none exists).","Twin Channel Assembly","Hot Metal Detectors (B101, B102)","HMD sensor failure, dirt/steam obscuring HMD lens, misalignment of HMD, electrical noise interference.","System incorrectly detects a bar not properly braked. Triggers upstream shear to crop unnecessarily. Production interruption and material waste.","Regular cleaning of HMD lenses. Verify HMD alignment and calibration. Shield HMDs from excessive steam/debris. Check for electrical noise sources.","Upstream shear performs a crop cut when no bar is physically present or expected at the HMD location. HMD status shows 'bar present' when channel is empty.","HMD_Status, ActualBarPresenceInChannel","Hot Metal Detector Signal","B101, B102","B101 or B102 is active (signal high) when visual confirmation or other sensor data indicates no bar is present."
"Twin Channel Auxiliary Systems Failure (Lubrication/Cooling for Drive)","Failure of lubrication or cooling for the twin channel drive motors or gearboxes.","Twin Channel Assembly","Lubrication Unit (JE11Y10CLC), Motor Cooling System (for M001-M008)","Failure of shared lubrication unit JE11Y10CLC (pump, filter, cooler). Low cooling water flow to motors (Mxxx-S914), clogged motor cooling filters (Mxxx-S913 water, Mxxx-S917 air).","Overheating and potential seizure/failure of twin channel drive motors or gearboxes.","Regular maintenance of lubrication unit JE11Y10CLC. Regular inspection and cleaning/replacement of motor cooling system components (filters, fans, water lines).","Alarms from JE11Y10CLC. High temperature alarms for twin channel motors (Mxxx-S912) or gearboxes (if monitored). Reduced cooling flow.","LubeUnitStatus, MotorTemperature, GearboxTemperature, CoolingFlowStatus","Temperature Sensors, Flow Switches, Pressure Switches (on Lube Unit)","Alerts from JE11Y10CLC, M00x-S912, M00x-S914, M00x-S913, M00x-S917","Fault alarms from lube unit. Motor/Gearbox temperatures rising. Cooling flow low."

</FAILURE_MODE_INFO>


<COBBLE_INFO>

## Cobble 

A "cobble" in this rolling mill refers to a severe disruption where the steel bar deviates from its intended path, leading to jams, buckling, folding, or breakage. This causes production stoppages, potential equipment damage, and safety risks.

### Causes of Cobble / Equipment & Factors Contributing to Cobbles:

The following details integrate specific sensor information and potential failure points related to cobble formation, with a particular focus on the Twin Channel and Tail Braker areas, as they are regions of primary interest for cobble prediction.

1.  **Speed Mismatches & Tension Issues:**
    *   **Stands (Roughing, Finishing, FFB):** Incorrect speed ratios are a primary cause.
        *   *Monitoring:* Actual motor speeds (e.g., M001 from various stand documents), speed references from the PLC (Section 3.1.1), and master speed settings. Discrepancies can indicate problems.
    *   **Loopers (Finishing Mill, FFB):** Malfunction disrupts tension management.
        *   *Monitoring:* Looper position sensors (e.g., `B001 LOOP CONTROL PHOTOCELL - POSITION` for a generic looper, or specific looper HMI status for height/enablement).
    *   **Pinch Rolls (Mill Entry, Shear Entry/Exit, FFB, Tail Braker):** Incorrect speed relative to adjacent equipment.
        *   *Monitoring:* Pinch roll motor speeds (e.g., `M001` for various pinch rolls like JD11B01TRU, JD51A02TRH), overspeed percentages (e.g., `PR0: Overspeed percentage`), and working diameters (e.g., `PR0: Working diameter`).
    *   **Tail Brakers (JE11A01FRT, JE11A02FRT):** Failure to match speed or brake correctly.
        *   *Monitoring:* `TB2_1A_ActualLinearSpeed` vs. `TB2_1A_SetLinearSpeed`, `TB2_1A_ActualTorquePct` vs. `TB2_1A_TorqueLimitPct`. Incorrect `TB2_1A_BrakingSpeedSel` or issues with closing pressure (`TB21A_ClsPressure`).
        *   *Specific Tags for Cobble Indication:* While no direct "cobble" tag is listed for tail brakers, erratic speed/torque, failure to achieve high pressure (`TB2_1A_HighPressureAchieveTime`), or misalignment detected by downstream `MATERIAL LINE 1A/1B - PRESENCE` (B001/B002) or Twin Channel HMDs could indicate a problem originating here.
    *   **Twin Channel (JE11A01CDD):** Speed mismatches during discharge.
        *   *Monitoring:* `TWC1A_ActualSpeed1/2` vs. `TWC1A_SpeedReference1/2`. `TWC1A_ActualTorque1/2` exceeding `TWC1A_TorqueLimit1/2`.
        *   *Specific Tag for Cobble Detection:* **`TWC1A_WORK_DB.CobbleDetect`** (Channel Cobble Detection) and **`Cobble detection in TWC-1`** (Line Cobble Detection) are direct indicators.
        *   *Contributing Factors:* Failure of the rotation mechanism indicated by discrepancies between `TWC1A_SetPosition1/2` and `TWC1A_ActPosition1/2`.

2.  **Guiding & Alignment Issues:**
    *   **Stand Guides:** Worn/improperly adjusted guides.
    *   **Shear Entry/Exit Funnels/Guides, Diverters (CVR, CVAH, CVSA):** Malfunction or incorrect timing.
        *   *Monitoring:* Status of diverter position (e.g., for Start/Stop Shear #1 - CVSD, `EXIT DIVERTER AT POSITION - ROLLING` S006). Failure of diverter to reach correct position.
    *   **Twin Channel Alignment:** Issues with channel arm assembly or central beam.
        *   *Monitoring:* `TWC1A_ActPosition1/2` for correct positioning. Visual inspection post-maintenance.

3.  **Equipment Malfunctions:**
    *   **Rolling Stands:** Bearing failures, roll breakage, screwdown issues (incorrect gap).
        *   *Monitoring:* Stand motor currents, bearing temperatures if monitored (not explicitly listed for all stands, but FFB bearings are via `MODULE X - ...BEARING (SHAFT X/Y) -B0Y#` tags like B101-B804), roll gap encoder feedback (e.g., `ROLLS GAP ADJUSTMENT POSITION CONTROL - FEEDBACK` B001 for DOM/DVM stands).
    *   **Shears (All Types):** Failure to cut, jams, incorrect timing.
        *   *Monitoring:* Shear motor currents (`M001` for Shear #1, #3), blade position feedback (`BLADES POSITION CONTROL - FEEDBACK` B001 for Shear #1), status of flywheel (`FLYWHEEL AT POSITION - COUPLED/UNCOUPLED` S004/S005 for Shear #1/#3).
    *   **Roller Tables/Transfers:** Drive failure, jammed rollers.
    *   **FFB:** Internal component failures.
        *   *Monitoring:* FFB motor drive status, lubrication system health (e.g., `FLOW ON GEARBOX LUBRICATION - MODULE X - MIN` like JD51FSL019111), bearing temperatures (B101-B804 for FFB lines).
    *   **Twin Channel:** Jamming during discharge.
        *   *Monitoring:* Directly by **`TWC1A_WORK_DB.CobbleDetect`**. Indirectly by motor torque/current (`TWC1A_ActualTorque1/2`, `TWC1A_ActCurrent1/2`) or failure to achieve set position (`TWC1A_ActPosition1/2`).
    *   **Tail Brakers:** Mechanical failure.
        *   *Monitoring:* Motor current (`TB2_1A_MotorCurrent`), torque values.

4.  **Material Issues:**
    *   **Temperature Variations:** Cold spots increase rolling force.
        *   *Monitoring:* Pyrometers at RHF exit and along the mill (e.g., `BILLET AT DESCALER - TEMPERATURE PYR` B101). `TWIN CHANNEL DRIVE LINE #1/2 - TEMPERATURE PYR` (B111, B112) and `TEMPERATURE DETECTION AT COOLING BED ENTRY 2ND NOTCH - TEMPERATURE PYR` (B112) are crucial for QTB/Cooling Bed entry.
    *   **Billet Defects/Hardness Variations.**

5.  **Control System & Sensor Failures:**
    *   **HMDs:** Critical for tracking.
        *   *Monitoring:* Status of HMDs (e.g., at furnace exit, before/after shears, `PR0: Enabling` which implies HMD for pinch roll control). Malfunction alarms. `Hot Metal Detector Raw/Filtered Signal` at Twin Channel entry.
    *   **Encoders (Motors, Shears, Stands):** Incorrect feedback disrupts control.
        *   *Monitoring:* Encoder fault alarms from PLC. `BLADES POSITION CONTROL - FEEDBACK` (B001) for Shear #1.
    *   **Loop Scanners:** Failure affects loop control.
    *   **Pyrometers:** Incorrect temperature readings.
    *   **Pressure/Flow Switches (Lube/Hyd/Fluids):** Can lead to equipment damage.
        *   *Tail Braker/Twin Channel Lubrication:* `TB_LUB_BushMinFlow`, `TWC_GREASE_PRESSURE_SWITCH_LINE-1`. `OIL LUBRICATION FLOW LINE 1A/1B - MIN` (S051/S052 for Tail Braker 1).
    *   **PLC/Automation Logic Errors.**


### Monitoring and Prevention Strategies:

1.  **Precise Speed & Tension Control:**
    *   **Cascade Speed Control:** Maintain speed ratios based on PLC logic and operator setpoints.
    *   **Loop Control:** Monitor `LOOP CONTROL PHOTOCELL - POSITION` (B001 for Vertical Loopers) and looper HMI status.
    *   **Tension Control (Roughing Mill):** Monitor motor torques (Actual values from stand drives) against HMI-set tension values (N/mm²).
    *   **Lead Speed:** Verify activation (e.g., `SH1: Shear head cut overspeed` for Shear 1).
    *   **Tail Braker Speed/Torque:** `TB2_1A_ActualLinearSpeed`, `TB2_1A_ActualTorquePct`, `TB2_1A_SetLinearSpeed`, `TB2_1A_TorqueLimitPct`.
    *   **Twin Channel Speed/Torque:** `TWC1A_ActualSpeed1/2`, `TWC1A_ActualTorque1/2`, `TWC1A_SpeedReference1/2`, `TWC1A_TorqueLimit1/2`.

2.  **Accurate Material Tracking:**
    *   **HMD Network:** Monitor HMD status on HMI. For Twin Channel, the entry HMDs (`Hot Metal Detector Raw/Filtered Signal`) are critical.
    *   **Speed Calculation & Calibration:**
        *   *Shear 1:* `SH1: Speed calibration enable`, `SH1: Bar speed correction` (`% 4.73`).
        *   *Chopping/Dividing Shears:* `CVR_1/2: Speed calibration enable`, `CVR_1/2: Bar speed correction` (`% 3.20 / 3.03`). `CVAH1/2: Speed calibration enable`, `CVAH1/2: Bar speed correction` (`% 4.96 / 4.97`). `SH3: Speed calibration enable`, `SH3: Bar speed correction` (`% 5.23`).

3.  **Continuity Control:**
    *   The system predicts arrival times based on tracking. Alarms trigger if material is not detected. This is a high-level function, direct tags are for the HMDs themselves.

4.  **Shear Interlocks and Control:**
    *   Monitor cut parameters (`SH1: Head cut length`, `CVR_1/2: Head cut length`, etc.) and overspeeds.
    *   Blade/diverter position feedback is crucial (e.g., `BLADES POSITION CONTROL - FEEDBACK` B001 for Shear #1).

5.  **Equipment Monitoring & Interlocks:**
    *   **Drive Faults:** General motor/drive fault alarms from PLC.
    *   **Lubrication/Hydraulics/Fluids:**
        *   *AirOil Lubrication for Stands:* `DISTR: Guides for stand X` (Enabled/Disabled status).
        *   *Tail Braker Lubrication:* `TB_LUB_TankOilTemperature`, `TB_LUB_DeliveryOilTemperature`.
        *   *Twin Channel Grease:* `TWC_GREASE_PRESSURE_SWITCH_LINE-1`.
    *   **Temperature Monitoring:**
        *   Billet Temperatures: `BILLET AT DESCALER - TEMPERATURE PYR` (B101).
        *   QTB/Cooling Bed Exit: `TWIN CHANNEL DRIVE LINE #1 - TEMPERATURE PYR` (B111), `TWIN CHANNEL DRIVE LINE #2 - TEMPERATURE PYR` (B112), `TEMPERATURE DETECTION AT COOLING BED ENTRY 2ND NOTCH - TEMPERATURE PYR` (B112).
    *   **Tail Braker Specific:**
        *   Klixon alarms: `BAR BRAKER DRIVE LINE #1/2 - Armature KLIXONS` (M00X-S902/S903), `BAR BRAKER DRIVE LINE #1/2 - Field KLIXONS` (M00X-S904/S905).
        *   Cooling: `BAR BRAKER DRIVE LINE #1/2 - Cooling WATER Temperature Thermostat` (M00X-S912), `BAR BRAKER DRIVE LINE #1/2 - Cooling Water Flow Switch` (M00X-S914).
        *   Roll Closing Pressure: `ROLLING CLOSING PRESSURE LINE 1A/1B/2A/2B` (B011-B014).
        *   Oil Pressure/Flow: `OIL LUBRICATION FLOW LINE 1A/1B/2A/2B - MIN` (S051-S054), `OIL PRESSURE LINE 1A/1B/2A/2B - MIN` (S011-S014).
    *   **Twin Channel Specific:**
        *   Safety: `TWC1A_WORK_DB.TWC_SafetyTrigger_ONS`.

6.  **Emergency Systems:**
    *   Snap Shear status (e.g., `SNAP SHEAR AT POSITION - OFF-LINE` S001 for FFB).
    *   General Emergency Stop system status (PLC level).

7.  **Operator Oversight & HMI:**
    *   Monitor HMI for actual vs. setup parameters, alarm statuses.
    *   *Crucial for Tail Braker/Twin Channel Cobbles:* `MATERIAL LINE 1A/1B/2A/2B - PRESENCE` (B001-B004 for Tail Braker) and HMDs at Twin Channel entry. If a bar is expected but not detected, or detected in an unexpected sequence, it can indicate a cobble.


--ADDITIONAL INFO ABOUT COBBLE
table with following columns give additional information regarding cobble

-component : component causing cobble,
-subcomponent : any subcomponent associted with cobble,
-cause : cause of the cobble,
-description : description of what happens,
-effect : effect of cobble on the system,
-generic_sensor : generic sensors that can detect the causes of cobble,
-specific_sensor : specific tags in the facility that can detect causes of cobble,
-sensor_trend : the trend detected by sensors

-TABLE DATA

"component","subcomponent","cause","description","effect","generic_sensor","specific_sensor","sensor_trend"
"Roughing Mill Stand","Drive System","Incorrect speed ratio between stands","One stand runs too fast or too slow relative to adjacent stands, causing pushing or pulling of the bar.","Bar buckling (if pushed) or stretching/breaking (if pulled), leading to cobble.","Speed Sensor, Motor Current Sensor, Torque Sensor, Loop Sensor (if applicable)","M001 (for stand), PLC Speed Reference, PLC Master Speed","Motor speeds deviate from setpoints/ratios; Loop sensor shows extreme high/low loop or tension control shows high correction; Motor current/torque spikes."
"Finishing Mill Looper","Position Control / Actuator","Looper malfunction (stuck, incorrect height)","Looper fails to maintain correct inter-stand tension by not forming or maintaining the loop correctly.","Excessive tension or slack between stands, leading to bar stretching/breaking or buckling/cobble.","Position Sensor, Proximity Switch","B001 LOOP CONTROL PHOTOCELL - POSITION, Looper HMI status (height, enabled)","Looper position sensor shows deviation from setpoint or no movement despite command; HMI status indicates fault."
"Pinch Roll (various)","Drive System","Incorrect pinch roll speed relative to adjacent equipment","Pinch roll speed not synchronized with upstream/downstream equipment, causing pushing or pulling.","Bar buckling or stretching, leading to cobble.","Speed Sensor, Motor Current Sensor","M001 (for pinch roll), PR0: Overspeed percentage, PR0: Working diameter","Pinch roll motor speed deviates from calculated setpoint; motor current spikes."
"Tail Braker","Drive System / Braking System","Incorrect speed matching or braking failure","Tail braker runs at a speed inconsistent with the incoming bar or fails to brake the bar appropriately before Twin Channel entry.","Bar enters Twin Channel too fast, too slow, or misaligned, causing a jam (cobble) in the Twin Channel.","Speed Sensor, Torque Sensor, Pressure Sensor (for roll closing)","TB2_1A_ActualLinearSpeed, TB2_1A_SetLinearSpeed, TB2_1A_ActualTorquePct, TB2_1A_TorqueLimitPct, TB21A_ClsPressure, B001/B002 (Material Line Presence downstream), TWC1A_WORK_DB.CobbleDetect","Actual speed deviates from set speed; Torque exceeds limits; Closing pressure not achieved. Downstream HMDs (TWC1A_WORK_DB.CobbleDetect) trigger."
"Twin Channel","Drive System","Speed mismatch of channel drive motors during bar discharge","Motors driving the Twin Channel discharge flaps/rollers are not synchronized or run at incorrect speeds.","Bar jams during discharge onto cooling bed, detected as cobble by Twin Channel sensors.","Speed Sensor, Torque Sensor, Position Sensor, Hot Metal Detector","TWC1A_ActualSpeed1/2, TWC1A_SpeedReference1/2, TWC1A_ActualTorque1/2, TWC1A_TorqueLimit1/2, TWC1A_WORK_DB.CobbleDetect, Cobble detection in TWC-1","Motor speeds deviate; Torque spikes; TWC CobbleDetect activates."
"Rolling Stand (Roughing/Finishing)","Guides","Worn or improperly adjusted stand guides","Guides fail to correctly direct the bar into the roll bite or out of the stand.","Bar miss-rolls, twists, or jams at stand entry/exit, leading to cobble.","Motor Current Sensor (stand), Visual Inspection","M001 (stand motor current)","Stand motor current spikes; HMDs downstream may show erratic signals or no material."
"Shear (e.g., Crop Shear #1)","Entry/Exit Funnel/Guide/Diverter","Malfunction or incorrect timing of shear guides/diverter","Guides or diverter fail to position correctly for bar passage or cutting, or timing is off.","Bar jams at shear, or cut pieces are not properly directed, leading to cobble.","Position Sensor (diverter), Motor Current Sensor (shear)","S006 (EXIT DIVERTER AT POSITION - ROLLING for CVSD), Shear motor current (M001)","Diverter position sensor shows incorrect state; Shear motor current spikes if jammed."
"Rolling Stand","Bearings / Rolls / Screwdown System","Mechanical failure of stand components (bearing seizure, roll breakage, incorrect roll gap)","A critical mechanical part of the stand fails, preventing proper rolling or passage of the bar.","Bar jams, breaks, or is improperly rolled, leading to cobble.","Motor Current Sensor, Temperature Sensor (bearing), Position Sensor (gap)","M001 (stand motor), B101-B804 (FFB bearing temps), B001 (DOM/DVM gap feedback)","Motor current spikes (seizure); Bearing temperature increases; Gap feedback deviates from setpoint."
"Shear (All Types)","Drive System / Blades / Control System","Shear fails to cut, jams, or cuts at the wrong time/length","Shear malfunction prevents timely or correct cutting of the bar.","Uncut bar continues, or improperly cut pieces cause jams downstream, leading to cobble.","Motor Current Sensor, Position Sensor (blades), HMD","M001 (Shear motor), B001 (Blades position feedback for Shear #1), S004/S005 (Flywheel status)","Shear motor current spikes (jam); Blade position incorrect; HMDs show unexpected bar presence/absence."
"Roller Table (e.g., Furnace Exit)","Drive Motor / Rollers","Roller table drive failure or jammed rollers","Roller table fails to transport the bar, causing a pile-up or stop.","Bar stops or jams on the roller table, leading to upstream cobble if material feed continues.","Motor Current Sensor, Speed Sensor","M001,M009 (Furnace Exit Roller Table motor)","Motor current spikes (jam) or drops (drive failure); Speed becomes zero."
"Fast Finishing Block (FFB)","Internal Rolling Modules/Bearings/Drives","Failure of internal FFB components (e.g., bearing seizure, module jam)","A critical component within the FFB fails, preventing bar passage or proper rolling.","Bar jams inside FFB, leading to cobble.","Motor Current Sensor, Temperature Sensor (bearings), Lubrication Flow/Pressure","M001/M002 (FFB motors), B101-B804 (FFB bearing temps), JD51FSL019111 (Lube flow)","FFB motor current spikes; Bearing temperatures rise; Lubrication flow/pressure drops."
"Rolled Bar","Material Property","Significant cold spots in the bar","Portions of the bar are much colder than expected, increasing rolling forces beyond equipment capacity or causing uneven deformation.","Increased rolling load can stall stands, cause bar to slip or jam, leading to cobble.","Pyrometer, Motor Current Sensor (stand)","B101 (Descaler Temp PYR), B111/B112 (Twin Channel Temp PYR), M001 (Stand motor current)","Pyrometer shows low temperature reading; Stand motor current spikes when cold spot enters."
"Rolled Bar / Billet","Material Property","Pre-existing billet defects or significant hardness variations","Inhomogeneities in the billet material lead to unpredictable behavior during rolling.","Uneven deformation, cracking, or breakage during rolling, leading to cobble.","Motor Current Sensor (stand), Visual Inspection","M001 (Stand motor current)","Stand motor current may show erratic behavior or spikes."
"Control System","Hot Metal Detector (HMD)","HMD malfunction (false positive/negative, no signal)","Incorrect bar presence/absence signals from HMDs lead to improper sequencing of equipment (e.g., shears, loopers, pinch rolls).","Equipment operates out of sync with material flow, causing jams, incorrect cuts, or tension issues, leading to cobble.","HMD Status, PLC Alarms","HMD tags (e.g., PR0: Enabling, HMD28_TWCA_ENTRY)","HMD status indicates fault or provides readings inconsistent with actual material flow; PLC alarms for HMD failure."
"Control System","Encoder","Encoder malfunction (incorrect speed/position feedback, no signal)","Faulty encoder data misinforms the control system about speed or position of critical equipment.","Incorrect speed synchronization, wrong cut lengths, improper loop control, leading to cobble.","Encoder Fault Signal, PLC Alarms","B001 (Blades position feedback for Shear #1), M001-B001 (Stand encoder)","PLC logs encoder fault; Equipment behaves erratically due to wrong feedback."
"Control System","Loop Scanner","Loop scanner malfunction (incorrect loop height reading, no signal)","Failure of loop scanner provides incorrect data for inter-stand tension control.","Improper loop formation, leading to excessive tension or slack, causing cobble.","Loop Scanner Status, PLC Alarms","B001 (LOOP CONTROL PHOTOCELL - POSITION)","Loop scanner HMI reading is erroneous or static; PLC alarms for scanner failure."
"Lubrication/Hydraulic/Fluid System","Pressure/Flow Switch","Failure of critical pressure/flow switch for support systems","Malfunction of a switch fails to detect low pressure/flow, leading to damage of primary equipment (e.g., stand bearings, gearbox).","Primary equipment (stand, shear, etc.) seizes or malfunctions due to lack of lubrication/hydraulic power, causing a cobble.","Pressure Switch Status, Flow Switch Status, PLC Alarms, Equipment Temperature/Current","TB_LUB_BushMinFlow, TWC_GREASE_PRESSURE_SWITCH_LINE-1, S051/S052 (Tail Braker Lube Flow)","Switch shows OK despite actual low flow/pressure; Subsequently, primary equipment motor current spikes, temperature rises, or HMDs detect stopped material."
"Twin Channel","Channel Arm Assembly / Channel Cavities","Insufficient gap for bar passage due to improper channel arm movement.","The channel arm assembly does not position correctly, creating a gap too small for the bar, leading to a jam within the Twin Channel.","Bar jams within the Twin Channel; Cobble detected.","Position Sensor, Hot Metal Detector","TWC1A_ActPosition1, TWC1A_SetPosition1, TWC1A_BarOutOfTailBraker, TWC1A_WORK_DB.CobbleDetect","TWC1A_ActPosition1 != TWC1A_SetPosition1 during operation; TWC1A_BarOutOfTailBraker may indicate bar entry but no exit; TWC1A_WORK_DB.CobbleDetect activates."
"Twin Channel","Rotating Shaft / Drive System","Jamming of the twin channel rotating shaft assembly.","The main rotating shaft of the twin channel jams, preventing the channel arm from discharging the bar to the cooling bed.","Bar cannot be discharged, backs up into the tail braker or preceding equipment, leading to a cobble upstream or within the twin channel.","Position Sensor, Motor Torque Sensor, Motor Speed Sensor, Hot Metal Detector (upstream)","TWC1A_ActPosition1, TWC1A_SetPosition1, TWC1A_ActualTorque1, TWC1A_ActualSpeed1, HMD28_TWCA_ENTRY (prolonged signal)","TWC1A_ActPosition1 does not change despite TWC1A_SetPosition1 changing; TWC1A_ActualTorque1 spikes; TWC1A_ActualSpeed1 drops to zero or very low; HMD at Twin Channel entry shows prolonged material presence."
"Twin Channel","Structural Frame / Central Beam","Breakage of structural links or the central beam of the twin channel.","A major structural failure in the twin channel leads to misalignment or collapse of the bar guiding path.","Bar severely misguides, jams, or the channel collapses, causing a major cobble and equipment damage.","Position Sensor, Hydraulic Pressure Sensor (if applicable), Vibration Sensor, Hot Metal Detector","TWC1A_ActPosition1, TWC1A_SetPosition1, Hydraulic Unit Pressure Alarms (if hydraulic actuation), TWC1A_WORK_DB.CobbleDetect","TWC1A_ActPosition1 shows erratic or impossible values; Hydraulic pressure might spike if movement is impeded; Vibration sensors (if present) show high levels; TWC cobble detectors activate."
"Twin Channel","Motor","Loss of power to the Twin Channel drive motor.","The motor responsible for moving the twin channel arm fails to operate due to lack of power.","Twin channel arm cannot move to discharge the bar, leading to bar backup and cobble upstream or within the channel.","Motor Current Sensor, Motor Speed Sensor, Position Sensor, Hot Metal Detector (upstream)","TWC1A_ActCurrent1, TWC1A_ActualSpeed1, TWC1A_ActPosition1, HMD28_TWCA_ENTRY (prolonged signal)","TWC1A_ActCurrent1 very low/zero despite command (TWC1A_SpeedReference1 > 0); TWC1A_ActualSpeed1 is zero; TWC1A_ActPosition1 unchanged."
"Twin Channel","Hydraulic Power Pack / Solenoid Coil","Failure of hydraulic pump or solenoid coil for twin channel actuation.","Lack of hydraulic pressure or control prevents the twin channel arm from moving.","Twin channel arm cannot discharge the bar, leading to bar backup and cobble upstream or within the channel.","Hydraulic Pressure Sensor, Position Sensor, Solenoid Status (if available), Hot Metal Detector (upstream)","Hydraulic Unit Pressure Alarms, TWC1A_ActPosition1, TWC1A_SetPosition1, HMD28_TWCA_ENTRY (prolonged signal)","Hydraulic pressure low alarm; TWC1A_ActPosition1 unchanged despite TWC1A_SetPosition1 changing."
"Tail Braker","Pinch Roller / Pneumatic System","Low pinch roller closing pressure.","Insufficient pressure applied by pinch rollers fails to grip or adequately brake the bar.","Bar passes through tail braker too quickly or slips, entering Twin Channel at excessive speed or misaligned, causing cobble in Twin Channel.","Pressure Sensor, Downstream Cobble Detector","TB21A_ClsPressure, TWC1A_WORK_DB.CobbleDetect","TB21A_ClsPressure below setpoint; TWC1A_WORK_DB.CobbleDetect activates."
"Tail Braker","Pinch Roller Assembly / Drive System / Gearbox","Mechanical failure preventing proper roller rotation or braking (bearing, roll surface, shaft, gearbox, motor).","Failure of critical mechanical components in the tail braker results in inability to control bar speed or guide it correctly.","Bar is not braked or guided properly, enters Twin Channel erratically (too fast, stalled, misaligned), causing cobble in Twin Channel.","Motor Torque Sensor, Speed Sensor, Temperature Sensor, Vibration Sensor, Downstream Cobble Detector","TB2_1A_ActualTorquePct, TB2_1A_ActualLinearSpeed, TB_LUB_DeliveryOilTemperature, M001-S912, TWC1A_WORK_DB.CobbleDetect","TB2_1A_ActualTorquePct spikes (seizure) or drops (no drive); TB2_1A_ActualLinearSpeed erratic or zero; Temperatures rise; TWC1A_WORK_DB.CobbleDetect activates."
"Tail Braker","Pneumatic System","Low air pressure or improper cylinder stroke in tail braker pneumatic system.","Malfunction in the pneumatic actuation of pinch rollers.","Ineffective braking due to insufficient pinch force, bar enters Twin Channel too fast, causing cobble.","Air Pressure Sensor, Cylinder Position (if available), Downstream Cobble Detector","TB_ACC_IN_AIR_PRESSURE, TB_ACC_OUT_AIR_PRESSURE, TB21A_ClsPressure, TWC1A_WORK_DB.CobbleDetect","Air pressure sensors low; TB21A_ClsPressure low; TWC1A_WORK_DB.CobbleDetect activates."
"Tail Braker","Guide Rollers","Misalignment of tail braker guide rollers.","Guide rollers are not correctly aligned, causing the bar to enter the Twin Channel off-center.","Bar enters Twin Channel misaligned, leading to jam/cobble in Twin Channel.","Visual Inspection, Downstream Cobble Detector","OperatorInput_BarMisalignedAtTailBraker, TWC1A_WORK_DB.CobbleDetect","TWC1A_WORK_DB.CobbleDetect activates."
"Tail Braker","Solenoid Valves (Control System)","Faulty solenoid valve for tail braker actuation.","Solenoid valve fails to operate correctly, leading to improper application or release of braking force.","Incorrect braking (too much, too little, wrong timing) causes bar to enter Twin Channel erratically, leading to cobble.","Solenoid Status (if available), Braking Performance Metrics, Downstream Cobble Detector","TB2_1A_RollsClose_solvalve_2, TB2_1A_HighPressClose_solvalve_2 (status not matching command), TWC1A_WORK_DB.CobbleDetect","Valve status contradicts command; Bar speed profile through tail braker is incorrect; TWC1A_WORK_DB.CobbleDetect activates."
"Tail Braker","Lubrication Cooling System","Overheating of tail braker lubrication oil due to cooling system failure.","Choked oil cooler, faulty oil pump, or choked oil filter leads to high oil temperature, potentially causing bearing/gearbox seizure in tail braker.","Tail braker seizes, stopping the bar abruptly, causing an upstream cobble or severe damage.","Oil Temperature Sensor, Oil Flow Sensor, Filter Differential Pressure Sensor, Motor Current (Tail Braker)","TB_LUB_DeliveryOilTemperature, TB_LUB_BushMinFlow, OilFilterDP_TailBraker (inferred), TB2_1A_MotorCurrent","TB_LUB_DeliveryOilTemperature rises significantly; TB_LUB_BushMinFlow drops or OilFilterDP high; Followed by TB2_1A_MotorCurrent spike if seizure occurs."


</COBBLE_INFO>

</BACKGROUND_INFO>

<EVENTS_HUMAN_NOTES>
This section provides descriptions of specific cobble incidents in the facility.
The descriptions are recorded by a human operator.

<SECOND_DESCRIPTION>

{data_from_capa_file}

</SECOND_DESCRIPTION>



</EVENTS_HUMAN_NOTES>

<INSTRUCTIONS>

--Carefully review the background information given between the tags <BACKGROUND_INFO> and </BACKGROUND_INFO>

--Background information contains specific information in sub sections. The sub sections are enclosed with in additional tags. The background information is organized as follows:

-Information about the entire Rolling Mill Facility is provided between the tags <FACILITY_INFO> and </FACILITY_INFO>. Provides overall information about the rolling mill facility.

-Information about the fault "cobble", causes, monitoring, prevention strategeis, sensors and tags that can detect are enclosed between the tags <COBBLE_INFO> and </COBBLE_INFO>.

-Cobble occurs in a sub area of the facility known as the Twin Channel Area. Detailed information about this area is provided between the tags <TWIN_CHANNEL_AREA_INFO> and </TWIN_CHANNEL_AREA_INFO>. Provides detailed information about the Twin Channel and associated Tail Braker areas.

-Sensor list for the twin channel and tail braker are provided between the tags <TWIN_CHANNEL_SENSORS> and </TWIN_CHANNEL_SENSORS> and <TAIL_BREAKER_SENSORS> and </TAIL_BREAKER_SENSORS> respectively.

-Failure modes of the twin channel and tail braker are provided between tags
<FAILURE_MODE_INFO> and </FAILURE_MODE_INFO>

-Based on background information, construct knowledge base required to analyze faults occurring in the system described. Focus on knowledge required to analyze incidents of
cobble.

--Carefully review the description of cobble event provided between the tags <EVENTS_HUMAN_NOTES> and </EVENTS_HUMAN_NOTES>


--Based on the cobble event described between the tags <EVENTS_HUMAN_NOTES> and </EVENTS_HUMAN_NOTES>, construct the following (based on background data, your knowledge):
-possible causes of the particular cobble event,
-components involved,
-failure modes,
-any recommendation for mitigating the cobble in the future,
-list of possible specific sesnors that may be used to investigate this particular cobble
-if multiple causes are inferred, create a list of specific sensors that can be used to detect each cause.
-the zone of the facility where the cobble occurred: did the cobble occur in the twin channel or tail braker area or
in the Fast Finish Block area. The Fast Finish Block has two lines with tags JD51A11BGV and JD51A21BGV. and these may be
mentioned in the description as "BGV"
-use only specific sensors from the sensor list provided in the background information to create the list of sensors. The sensor
lise is provided between 
--the tags <TWIN_CHANNEL_SENSORS> and </TWIN_CHANNEL_SENSORS> and
--the tags <TAIL_BREAKER_SENSORS> and </TAIL_BREAKER_SENSORS>.
-DO NOT CREATE ANY NEW SENSORS. USE ONLY THE SENSORS PROVIDED IN THE BACKGROUND INFORMATION.
</INSTRUCTIONS>

<TASK>

-Analyze the cobble incident described between the tags <EVENTS_HUMAN_NOTES> and </EVENTS_HUMAN_NOTES>.
-Figure out possible causes, components involved, failure modes, specific tags and additional information
-Provide a detailed analysis and the rationale for the causes you determine.
-Use only specific sensors from the background information to create the list of sensors
-sensor list is provided under section
-- TAIL BRAKER SENSORS TABLE DATA
between the tags  <TAIL_BREAKER_SENSORS> and </TAIL_BREAKER_SENSORS>.

-- TWIN CHANNEL SENSORS TABLE DATA
between the tags <TWIN_CHANNEL_SENSORS> and </TWIN_CHANNEL_SENSORS>


</TASK>

<OUTPUT_FORMAT>
If can not determine information for any field, simply leave the value blank.
In strict JSON format with following fields:


    equipment_details : <string> details about the equipment or location involved in the cobble,
    
    summary : <string> summary description of the cobble event,
    
    cause : <string> cause of the cobble event, if multiple causes, list all, separated by '\n'. Try the use the casues from the
    table provided in the background information, between the tags <FAILURE_MODE_INFO> and </FAILURE_MODE_INFO>.
    
    component : <string> componenet involved in the cobble,
    
    failure_mode : <string> failure mode that caused cobble, please use a failure mode from the table provided in the background information,
    between the tags <FAILURE_MODE_INFO> and </FAILURE_MODE_INFO>.

    facility_zone : <string> facility zone where the cobble event occurred. If the description mentions twin channel or tail braker area as the
    location of cobble, use "TCTB" as the value. If the description mentions Fast Finish Block or BGV is mentioned in the description, use "FFB" as the value. 
    If the zone can not be determined, use the value "UNKNOWN".
    
    reasoning_rationale : <string> a very detailed rationale of the reasoning that determined the cause or causes,
    
    recommendations : <string> any recommendations for mitigating the effect,
    
    equip_op_status : <string> operational status of the equipment or component during cobble,
    
    user_summary_two : <string> summarize the description provided between the tags <SECOND_DESCRIPTION> and </SECOND_DESCRIPTION>,
    
    tags_set_one : <list> List of names of specific sensors that may be used to detect cobble for the first cause, 
    
    tags_rationale_one : <string>reasoning behind the choice of sensors for detecting cobble for the first cause,
    
    tags_set_two : <list> List of names of specific sensors that may be used to detect cobble for the second cause. Leave blank if there is no second cause,
    
    tags_rationale_two : <string> reasoning behind the choice of sensors for detecting cobble for the second cause. Leave blank if there is no second cause,
    
    tags_set_three : <list> List of names of specific sensors that may be used to detect cobble for the third cause. Leave blank if there is no third cause, ,
    
    tags_rationale_three : <string> reasoning behind the choice of sensors for detecting cobble for the second cause. Leave blank if there is no second cause.

    

</OUTPUT_FORMAT>
"""

