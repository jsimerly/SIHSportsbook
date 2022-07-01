import React, { useState } from "react";
import { 
    Grid,
    Box,
    ToggleButton
} from "@mui/material";

import impliedOddsToAmerican from "../../util/oddHandler";

export default function BetTile(props){
    const matchupData = props.matchupData;
    const team = props.team;
    const betType = props.betType;
    const betValue = props.matchupData.data[props.betType]

    function vanityLogic() {
        if (betType === "spread_team1" || betType === "spread_team2") {
            if (props.data > 0) {
                return [
                    team + " " + betValue,
                    "Spread",
                    "+" + props.data,
                ]
            } 
            return [
                team + " " + betValue,
                "Spread",
                props.data,
            ]
    
        } else if (betType === "over") {
            return [
                "Over " + betValue,
                "Total",
                "O " + props.data,
            ]
        }  else if (betType === "ml_team1" || betType === "ml_team2") {
            return [
                team,
                "Moneyline",
                impliedOddsToAmerican(props.data),
            ]
        } else if (betType === "under") {
            return [
                "Under " + betValue,
                "Total",
                "U " + props.data
            ]
        }

        return ["ERROR", "ERROR", "ERROR"]
    }
    
    const vanityTeams = (props.matchupData.data.team1 + " @ " + props.matchupData.data.team2)
    const [ vanityMain, vanitySecondary, vanityValue] = vanityLogic()
    const americanOdds = impliedOddsToAmerican(props.betOdds)  

    const bet = {
        matchupData,
        betData : {
            betType : betType,
            betValue : betValue,
            team: team,
            odds: props.betOdds,
            wager: 0,
        },
        vanity: {
            main: vanityMain,
            secondary: vanitySecondary,
            teams: vanityTeams,
            value: vanityValue,
            line: americanOdds,
        },
    }

    function buttonSelected() {
        props.betSelectedHandler(bet)
    }

    function isSelectedBet() {
        const dupIndex = props.checkDupsIndex(props.selectedBets, bet)
        if (dupIndex != -1) {
            return true
        } else {
            return false
        }
    }

    function BetButton() {
        return (<ToggleButton
            fullWidth={true} 
            value={props.data}

            selected={isSelectedBet()}
            onChange={buttonSelected}
        >
            {vanityValue}
        </ToggleButton>)
    }

    return (
        BetButton()
    )
}