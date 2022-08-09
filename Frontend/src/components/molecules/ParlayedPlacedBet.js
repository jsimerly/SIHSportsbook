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
import ParlayDetails from "../atoms/parlayDetails";
import CircleTwoToneIcon from '@mui/icons-material/CircleTwoTone';


export default function ParlayedPlacedBets(props){
        return(
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
                                    Parlay ({props.bet.bets.length}-leg)
                                </Box>
                                <Box>
                                    Wager: ${props.bet.wager}
                                </Box>
                                <Box>
                                    To Win: ${props.bet.to_win}
                                </Box>
                            </Grid>
                          
                        </Grid>
                </AccordionSummary>
                <AccordionDetails>
                    <Divider sx={{mb:1}}/>
                    <Grid>
                        {props.bet.bets.map((bet, index) => 
                            <ParlayDetails
                                bet={bet}
                            />
                        )}
                        <Box>
                            4
                        </Box>
                    </Grid>
                </AccordionDetails>
            </Accordion>
            
        ) 
 }