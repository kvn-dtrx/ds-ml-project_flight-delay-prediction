# DS ML Project: Flight Delay Prediction

## Synopsis

This repository contains our analysis of the [flight delay dataset for Tunisair](https://zindi.africa/competitions/flight-delay-prediction-challenge) from [Zindi](https://zindi.africa).

The general exercise reads as follows:

> **Value of Product**: Build a flight delay predictive model using Machine Learning techniques. The accurate prediction of flight delays will help all players in the air travel ecosystem to set up effective action plans to reduce the impact of the delays and avoid loss of time, capital and resources.

We try to predict the flight delay duration in $\mathrm{min}$. We evaluate our models with the root mean square error ($\mathrm{RMSE}$), in alignment with the requirements of the challenge.

As a baseline model, we choose a **linear regression** using weekday as predictor for flight delays, resulting in a $\mathrm{RMSE}$ of approximately $114$.

As the main ML model, we employ **CatBoost** that is suited for situations where the majority of features is categorical, resulting in a $\mathrm{RMSE}$ of approximately $96$.

<!-- 
NOTE: Correct LaTeX usage here would be `\operatorname` instead of `\mathrm`. 
But GitHub cannot render the former macro.
-->

## Repository Organisation

The organisation of the repository follows common conventions and therefore requires little explanation. Let us only mention that our analysis notebooks (with technical details) are subordinated to [`notebooks/`](./notebooks/) and that our presentation slides for a non-technical audience can be found in [`docs/`](./docs/).

## Installation

### Requirements

- Python 3.11.3
- pyenv

### Setup

1. Navigate to a working directory of your choice, then clone the repository and enter it:

   ``` shell
   git clone https://github.com/kvn-dtrx/ds-ml-project_flight-delay-prediction.git &&
       cd ds-ml-project_flight-delay-prediction
   ```

2. Choose the right setup option based on your operating system:

   - `make unix`: macOS/Linux.
   - `make win`: Windows (PowerShell).

   If you prefer to run the commands manually yourself or want to inspect what a `make` target does first, use the `-n` flag for a dry run. This prints the commands without executing them:

   ``` shell
   make -n <target>
   ```

3. Activate the virtual environment:

   - On macOS/Linux, run:

     ```shell
     source .venv/bin/activate
     ```

   - On Windows (PowerShell), run:

     ``` powershell
     .\.venv\Scripts\Activate.ps1
     ```

## Colophon

**Authors:** [MoSeBaur](https://github.com/MoSeBaur), [greseberisha](https://github.com/greseberisha), [kvn-dtrx](https://github.com/kvn-dtrx)

**Template:** This repository was instantiated from the [Neue Fische DS/ML Project Template](https://github.com/neuefische/ds-ml-project-template).

**License:** [MIT License](license.txt)
