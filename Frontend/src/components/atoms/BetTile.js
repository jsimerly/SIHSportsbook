import React, { Component, useState } from "react";
import { 
    Grid,
    Box,
    ToggleButton
} from "@mui/material";

export default function BetTile(props){
    const [selectedBool, setSelected] = useState(false);

    function buttonSelected(event) {
        setSelected(!selectedBool);
        props.betHandler(props.betType)
    }

    function BetButton(text) {
        return (<ToggleButton
            fullWidth={true} 
            value={props.data}
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