import React, { Component, useState } from "react";
import { 
    Grid,
    Box,
    TextField,
    IconButton,
} from "@mui/material";

export default function PlacedBets(props){
    function getCorrectBet(bet){
        if (bet.bet_type === "M1" || bet.bet_type === "M2"){
            return (
                <Box>
                    {bet.subtype_info.team1} - {bet.subtype_info.team2}
                </Box>
            )
        } else if (bet.bet_type === "O"){
            return (
                <Box>
                    OPEN
                    {bet.subtype_info.team1} - {bet.subtype_info.team2}
                </Box>
            )
        } else {
            return (
                <Box>
                   <Grid container sx={{border:1}}>
                     123
                   </Grid>
                </Box>
            )
        }
    }
    return (
       getCorrectBet(props.bet)
    )
 }