import React, { Component } from "react";
import { 
    Grid,
    Box,
    ToggleButton
} from "@mui/material";

export default function BetTile(props){
    const betTileButton = (
        <ToggleButton fullWidth={true}>
            {props.betValue}
        </ToggleButton>
    )

    return (
        <div>
            {betTileButton}
        </div>
    )
}