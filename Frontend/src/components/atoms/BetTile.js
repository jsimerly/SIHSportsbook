import React, { useState } from "react";
import { 
    Grid,
    Box,
    ToggleButton
} from "@mui/material";

export default function BetTile(props){
    const matchupData = props.matchupData;
    const team = props.team;
    const betType = props.betType;
    const betValue = props.matchupData.data[props.betType]

    function vanityLogic() {
        if (betType === "sp_pos") {
            return [
                team + " " + betValue,
                "Spread"
            ]
        } else if (betType === "over") {
            return [
                "Over " + betValue,
                "Total"
            ]
        }  else if (betType === "ml_pos" || betType === "ml_neg") {
            return [
                team,
                "Moneyline"
            ]
        } else if (betType === "sp_neg") {
            return [
                team + " " + betValue,
                "Spread"
            ]
        } else if (betType === "under") {
            return [
                "Under " + betValue,
                "Total"
            ]
        }

        return ["ERROR", "ERROR"]
    }

    function vanityTeams() {
        return (props.matchupData.data.team1 + " @ " + props.matchupData.data.team2)
    }

    let [ vanityMain, vanitySecondary ] = vanityLogic()

    function setLine(){
        if (betType === "ml_pos" || betType === "ml_neg") {
            return (betValue)
        } else {
            return (matchupData.standardLine)
        }
    }

    const line = setLine()

    function setVanityLine(){
        if (line > 0) {
            return ("+" + line)
        } else {
            return (line)
        }
    }

    let bet = {
        matchupData,
        betData : {
            betType : betType,
            betValue : betValue,
            team: team,
            line: setLine()
        },
        vanity: {
            main: vanityMain,
            secondary: vanitySecondary,
            teams: vanityTeams(),
            line: setVanityLine()
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

    function BetButton(text, team) {
        return (<ToggleButton
            fullWidth={true} 
            value={props.data}

            selected={isSelectedBet()}
            onChange={buttonSelected}
        >
            {text}
        </ToggleButton>)
    }

    function ifButton() {
        if (props.betType === "over") {
            const text = "O " + props.data
            return (
                BetButton(text)
            )
        } else if (props.betType === "under") {
            const text = "U " + props.data
            return (
                BetButton(text)
                )
        } else if (props.betType === "ml_pos"){
            const text = "+" + props.data
            return (
                BetButton(text)
                )
        } else {
            const text = props.data
            return (
                BetButton(text)
            )
        }
    }

    return (
        ifButton()
    )
}