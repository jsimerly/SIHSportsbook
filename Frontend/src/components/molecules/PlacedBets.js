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
    
    return (
        <RegBetSlipOpen
            betValue = 'Jared Cannonier'
            betType = 'MONEYLINE'
            statusColor = 'grey'
            status = 'OPEN'
            event = 'Israel Adesanya vs Jared Cannonier'
            bet = {props.bet}
        />
    )
 }