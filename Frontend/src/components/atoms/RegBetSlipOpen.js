import React, { Component, useState } from "react";
import { 
    Grid,
    Box,
    Accordion,
    AccordionDetails,
    AccordionSummary,
    Divider,
} from "@mui/material";
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import CircleTwoToneIcon from '@mui/icons-material/CircleTwoTone';

export default function RegBetSlipOpen(props){
    console.log('++++++++++++')
    console.log(props.bet)
    return (
        <Accordion>
                <AccordionSummary
                    expandIcon={<ExpandMoreIcon/>}
                >
                 
                    <Grid container>
                        <Grid item xs={1}>
                            <CircleTwoToneIcon sx={{color : props.statusColor, fontSize : 10}}/>
                        </Grid>
                        <Grid item xs={11}>
                            <Box>
                                {props.betValue}
                            </Box>
                            <Box>
                                {props.betType}
                            </Box>
                            <Box>
                                Wager: ${props.bet.wager.toFixed(2)}
                            </Box>
                            <Box>
                                To Win: ${props.bet.payout_amount.toFixed(2)}
                            </Box>
                            
                        </Grid>
                    </Grid>
                </AccordionSummary>
                <AccordionDetails>
                    <Divider sx={{mb:1}}/>
                    <Grid container>
                        <Grid item xs={10}>
                            <Box>
                                {props.status}
                            </Box>
                            <Box>
                                {props.event}
                            </Box>
                            <Box>
                                {props.bet.payout_date}
                            </Box>
                        </Grid>
                        <Grid item xs={2} sx={{pl:1.5}}>
                            <Box>
                                {props.bet.line}
                            </Box>
                        </Grid>
                    </Grid>
                </AccordionDetails>
            </Accordion>
    )
}