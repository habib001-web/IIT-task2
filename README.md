# AMD Stock Share Analysis

A professional web application for analyzing SEC-reported common stock shares outstanding data for Advanced Micro Devices (AMD) and other publicly traded companies.

## Project Overview

This project fetches and displays stock share outstanding data from the SEC EDGAR database, focusing on fiscal years after 2020. It provides a clean, interactive interface to view maximum and minimum shares outstanding with dynamic company switching capabilities.

## Features

- **SEC Data Integration**: Fetches real-time data from SEC EDGAR XBRL API
- **Dynamic Company Switching**: Support for querying any company via CIK parameter
- **Responsive Design**: Beautiful gradient-based UI that works on all devices
- **Data Processing**: Automatic filtering and analysis of fiscal year data
- **Static Data Fallback**: Includes pre-processed data.json for offline access

## Setup Instructions

### Prerequisites

- Python 3.6+ (for data fetching script)
- Modern web browser (for viewing the application)
- Internet connection (for live SEC data fetching)

### Installation

1. Clone or download this repository
2. No additional dependencies required - uses Python standard library and vanilla JavaScript

### Running the Data Fetch Script