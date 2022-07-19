import React, { Component, useState } from "react";
import { 
    Grid,
    Box,
    TextField,
    IconButton,
} from "@mui/material";
import RemoveCircleOutlineIcon from '@mui/icons-material/RemoveCircleOutline';
import BetSlipTile from "../atoms/BetSlipTile";

export default function ParlayedPlacedBets(props){

    function getCorrectBet(bet){
        if (bet.bet_type === "M1" || bet.bet_type === "M2"){
            return (
                <Box>
                    {bet.subtype_info.team1} - {bet.subtype_info.team2}
                    1
                </Box>
            )
        } else if (bet.bet_type === "O"){
            return (
                <Box>
                    OPEN
                    2
                    {bet.subtype_info.team1} - {bet.subtype_info.team2}
                </Box>
            )
        } else {
            return (
                <Box>
                    <Grid container sx={{border:1, p:1}}>
                        <Grid item xs={10}>
                            <Box>
                                Jared Cannonier
                            </Box>
                            <Box>
                                MONEYLINE
                            </Box>
                            <Box>
                                Wager: $100
                            </Box>
                        </Grid>
                        <Grid item xs={2}>
                            WON
                        </Grid>
                    </Grid>
                </Box>
            )
        }
    }
    return (
       getCorrectBet(props.bet)
    )
 }