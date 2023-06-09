# LoRaWAN Node Based Outdoor Air System

This repository contains the source code and documentation for the LoRaWAN Node Based Outdoor Air System (OAS). The OAS is a system designed to accurately monitor levels of particulate matter (PM) dust particles, temperature, and humidity in outdoor environments using LoRaWAN technology.

## Table of Contents
- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Materials](#materials)
- [Methods](#methods)
- [Conclusion](#conclusion)
- [License](#license)

## Introduction
The LoRaWAN Node Based Outdoor Air System aims to provide real-time air quality monitoring in both urban and rural areas. By leveraging LoRaWAN technology, the system allows for the deployment of multiple sensing nodes that transmit data wirelessly to a central gateway. This repository contains the source code and documentation for the project, including hardware specifications, software tools, data collection methods, and project conclusions.

## Project Overview
The project utilizes LoRaWAN technology to establish a network of nodes for data collection. Each node is equipped with a microcontroller, a LoRaWAN-compatible transmitter, and a SEN54 particle sensor. The nodes communicate with a LoRaWAN Gateway connected to The Things Network Cloud (TTN) for data transmission and processing. The collected data is then made accessible through a local Python web server for analysis.

## Materials
The hardware components used in the OAS system include:
- Dragino LoRaWAN Gateway
- SEN54 particulate matter, temperature, and humidity sensor
- Arduino Zero microcontroller
- Dragino LoRaWAN Arduino shield

The software tools used in the OAS system include:
- Arduino Integrated Development Environment (IDE)
- The Things Network Cloud (TTN)
- Python 3.7

## Methods
The data collection process involves wirelessly transmitting data from each node to the Dragino Gateway, which then forwards it to the Things Network Cloud (TTN) for processing. The collected data includes readings from particle, temperature, and humidity sensors. Multiple nodes can be deployed in a target area to provide a comprehensive understanding of air quality across different locations.

The system also allows for node logistics, where the nodes are configured to be powered by a battery bank, enabling their deployment in various locations. The system has been tested in different environments, including indoor and outdoor settings, to capture diverse conditions and provide a more accurate assessment of air quality.

## Conclusion
The development of the LoRaWAN Node Based Outdoor Air System has successfully demonstrated its potential for real-time air quality monitoring. The system's multiple nodes connected to a central gateway enhance the accuracy and reliability of air quality data collection. The findings from this study confirm the feasibility of the system and lay the foundation for further advancements in this field.

## License
This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code as per the terms of the license.

Please refer to the individual files and directories for specific license information related to the included libraries and dependencies.

**Note:** This README provides a high-level overview of the project. For detailed information, refer to the project documentation available in the repository.
