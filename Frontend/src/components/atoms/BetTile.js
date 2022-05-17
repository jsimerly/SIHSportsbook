import React, { Component, useState } from "react";
import { 
    Grid,
    Box,
    ToggleButton
} from "@mui/material";

export default function BetTile(props){
    const [selectedBool, setSelected] = useState(false);

    function buttonSelected(e) {
        setSelected(!selectedBool);
        const team = e.target.title
        props.betHandler(props.betType, team)
    }

    function BetButton(text, team) {
        return (<ToggleButton
            fullWidth={true} 
            value={props.data}
            title={team}

            selected={selectedBool}
            onChange={buttonSelected}
        >
            {text}
        </ToggleButton>)
    }

    function ifButton() {
        if (props.betType === "over") {
            const text = "O " + props.data
            return (
                BetButton(text, null)
            )
        } else if (props.betType === "under") {
            const text = "U " + props.data
            return (
                BetButton(text, null)
                )
        } else if (props.betType === "ml_pos"){
            const text = "+" + props.data
            return (
                BetButton(text, props.team)
                )
        } else {
            const text = props.data
            return (
                BetButton(text, props.team)
            )
        }
    }

    return (
        ifButton()
    )
}