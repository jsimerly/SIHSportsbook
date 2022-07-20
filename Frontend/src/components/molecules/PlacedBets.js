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
import OpenBetSlipReg from "../atoms/openBetSlipReg";

export default function PlacedBets(props){
    
    return (
        <OpenBetSlipReg 
            betValue = 'Jared Cannonier'
            betType = 'MONEYLINE'
            statusColor = 'grey'
            bet = {props.bet}
        />
    )
 }