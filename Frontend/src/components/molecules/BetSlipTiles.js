import React, { Component, useState } from "react";
import { 
    Grid,
    Box,
    TextField,
    IconButton,
} from "@mui/material";
import RemoveCircleOutlineIcon from '@mui/icons-material/RemoveCircleOutline';
import BetSlipTile from "../atoms/BetSlipTile";

export default function BetSlipTiles(props){

    return (
        <Box>
            {props.selectedBets.map((bet, index) => {
                return (
                    <BetSlipTile
                        bet={bet}
                        handleRemoveBet={props.handleRemoveBet}
                        handleWager={props.handleWager}
                    /> 
                )
            })}
        </Box>
    )
 }
