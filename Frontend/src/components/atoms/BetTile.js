import React, { Component, useState } from "react";
import { 
    Grid,
    Box,
    ToggleButton
} from "@mui/material";

export default function BetTile(props){
    const betData = props.betData
    const [selectedBool, setSelected] = useState(false);

    function buttonSelected() {
        setSelected(!selectedBool);
    }

    function BetButton(text) {
        return (<ToggleButton
            fullWidth={true} 
            value={props.betValue}
            selected={selectedBool}
            onChange={buttonSelected}
        >
            {text}
        </ToggleButton>)
    }

    function main() {
        if (props.type === "over") {
            const text = "O " + props.betData
            return (
                BetButton(text)
            )
        } else if (props.type === "under") {
            const text = "U " + props.betData
            return (
                BetButton(text)
                )
        } else if (props.type === "pos"){
            const text = "+" + props.betData
            return (
                BetButton(text)
                )
        } else {
            const text = props.betData
            return (
                BetButton(text)
            )
        }
    }

    return (
        main()
    )
}