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

export default function OpenBetSlipReg(props){
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
                                {props.bet.wager}
                            </Box>
                            
                        </Grid>
                    </Grid>
              
                </AccordionSummary>
                <AccordionDetails>
                    <Grid container>
                        <Grid item xs={10}>
                            <Box>

                            </Box>
                        </Grid>
                        <Grid item xs={2}>
                            {props.status}
                        </Grid>
                    </Grid>
                </AccordionDetails>
            </Accordion>
    )
}