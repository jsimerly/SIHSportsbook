import React, { Component, useState } from "react";
import { 
    Grid,
    Box,
    TextField,
    IconButton,
} from "@mui/material";
import RemoveCircleOutlineIcon from '@mui/icons-material/RemoveCircleOutline';
import BetSlipTile from "../atoms/BetSlipTile";
import CircleTwoToneIcon from '@mui/icons-material/CircleTwoTone';

export default function ParlayDetails(props){
    let betType 
    let betValue
    let event

    if (props.bet.type === 'FFM'){
        if (props.bet.bet_type === 'M1'){
            betValue = props.bet.subtype_info.team1
            betType = 'MONEYLINE'
        } else if (props.bet.bet_type === 'M2'){
            betValue = props.bet.subtype_info.team2
            betType = 'MONEYLINE'
        } else {
            betValue = props.bet.bet_value
            betType = props.bet.bet_type
        }

       event = props.bet.subtype_info.team1 + ' vs ' + props.bet.subtype_info.team2
    }

    return (
        <Grid container sx={{pl:2}}>
            <Grid item xs={1} justifyContent="center">
                <CircleTwoToneIcon sx={{color : props.statusColor, fontSize : 10}}/>
            </Grid>
            <Grid item xs={10}>
                <Box>
                    {betType}
                </Box>
                <Box>
                    {betValue}
                </Box>
                <Box>
                    {event}
                </Box>
            </Grid>
            <Grid item xs={1}>
                {props.bet.line}
            </Grid>
        </Grid>
        
    )
 }
