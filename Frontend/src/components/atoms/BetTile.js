import React, { Component } from "react";
import { 
    Grid,
    Box,
    ToggleButton
} from "@mui/material";

export default function BetTile(props){
    const betData = props.betData

    function main() {
        if (props.type === "over") {
            return (
            <ToggleButton fullWidth={true} value={props.betValue} aria-label="t1">
                O {props.betData}
            </ToggleButton>
            )
        } else if (props.type === "under") {
            return (
                <ToggleButton fullWidth={true} value={props.betValue} aria-label="t1">
                    U {props.betData}
                </ToggleButton>
                )
        } else {
            return (
                <ToggleButton fullWidth={true} value={props.betValue} aria-label="t1">
                    {props.betData}
                </ToggleButton>
            )
        }
    }

    console.log(props.type)

    return (
        main()
    )
}