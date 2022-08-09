import React, { Component, useState } from "react";
import { 
    Grid,
    Box,
    Accordion,
    AccordionDetails,
    AccordionSummary,
} from "@mui/material";
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import CircleTwoToneIcon from '@mui/icons-material/CircleTwoTone';
import RegBetSlipOpen from "../atoms/RegBetSlipOpen";

export default function PlacedBets(props){
    let betValue = 'Error'
    let betType = 'Error'
    let event = 'Error'

    const betStatusMap = {
        'O' : 'Open',
        'W' : 'Won',
        'L' : 'Lost',
        'R' : 'Refunded',
        'C' : 'Cashed Out'
    }

    const betStatusColorMap = {
        'O' : 'grey',
        'W' : 'green',
        'L' : 'red',
        'R' : 'white',
        'C' : 'yellow'
    }

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
        <RegBetSlipOpen
            betValue = {betValue}
            betType = {betType}
            statusColor = {betStatusColorMap[props.bet.status]}
            status = {betStatusMap[props.bet.status]}
            event = {event}
            bet = {props.bet}
        />
    )
 }