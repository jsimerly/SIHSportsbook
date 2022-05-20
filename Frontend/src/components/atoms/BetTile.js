import React, { Component, useState } from "react";
import { 
    Grid,
    Box,
    ToggleButton
} from "@mui/material";

export default function BetTile(props){
    const matchupData = props.matchupData
    const team = props.team;
    let bet = {
        matchupData,
        betData : {
            betType : props.betType,
            betValue : props.matchupData.data[props.betType],
            team: team,
        }
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