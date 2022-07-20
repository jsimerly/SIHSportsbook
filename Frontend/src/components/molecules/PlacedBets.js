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
    let betStatus = 'Error'
    let betStatusColor = 'grey'

    if (props.bet.type === 'FFM'){
        if (props.bet.bet_type === 'M1'){
            betValue = props.bet.subtype_info.team1
            betType = 'MONEYLINE'
        } else if (props.bet.bet_type === 'M2'){
            betValue = props.bet.subtype_info.team2
            betType = 'MONEYLINE'
        } else if (props.bet.bet_type === 'O') {
            betType = 'Over'
        } else if (props.bet.bet_type === 'U') {
            betType = ''
        } else if (props.bet.bet_type === 'O') {
            betType = 'Over'
        } else if (props.bet.bet_type === 'O') {
            betType = 'Over'
        }
    }
    
    return (
        <RegBetSlipOpen
            betValue = {betValue}
            betType = {betType}
            statusColor = {betStatusColor}
            status = {betStatus}
            event = 'Israel Adesanya vs Jared Cannonier'
            bet = {props.bet}
        />
    )
 }