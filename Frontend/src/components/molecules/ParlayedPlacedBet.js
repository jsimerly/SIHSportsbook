import React, { Component, useState } from "react";
import { 
    Grid,
    Box,
    Accordion,
    AccordionDetails,
    AccordionSummary,
} from "@mui/material";
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';


export default function ParlayedPlacedBets(props){
    function betSlipTemplate(betValue, betType, wager, status, result, line, payoutDate){
        return(
            <Accordion>
                <AccordionSummary
                    expandIcon={<ExpandMoreIcon/>}
                >
                    <Box>
                        <Grid container>
                            <Grid item>
                                <Box>
                                    Parlay (3-leg)
                                </Box>
                                <Box>
                                    {betType}
                                </Box>
                                <Box>
                                    {wager}
                                </Box>
                            </Grid>
                          
                        </Grid>
                    </Box>
                </AccordionSummary>
                <AccordionDetails>
                    <Grid container>
                        <Grid item xs={10}>
                            1
                        </Grid>
                        <Grid item xs={2}>
                            2
                        </Grid>
                    </Grid>
                </AccordionDetails>
            </Accordion>
            
        )
    }

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
       betSlipTemplate('Jared Cannonier', 'MONEYLINE', 'Wager: $100', 'OPEN', '5:5')
    )
 }