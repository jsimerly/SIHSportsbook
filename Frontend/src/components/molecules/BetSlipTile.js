import React, { Component, useState } from "react";
import { 
    Grid,
    Box,
    TextField
} from "@mui/material";


export default function BetSlipTile(props){
    return (
        <Box sx={{border:1}}>
            <Box sx={{mb:1}}>
                <Grid container>
                    <Grid item xs={1} sx={{p:1}}>
                        -
                    </Grid>
                    <Grid item xs={11}>
                        <Box>
                            <Grid container>
                                <Grid item xs={9}>
                                    {props.betData.betData.betValue}
                                </Grid>
                                <Grid item xs={3}>
                                    -110
                                    {/* calculate using vig */}
                                </Grid>
                            </Grid>
                        </Box>
                        <Box>
                            Total Points
                        </Box>
                        <Box sx={{fontSize:10}}>
                            <Grid container>
                                <Grid item xs={9}>
                                    {props.betData.matchupData.data.team1} @ {props.betData.matchupData.data.team2}
                                </Grid>
                                <Grid item xs={3}>
                                    {props.betData.matchupData.payoutDate}
                                </Grid>
                            </Grid>
                        </Box>
                    </Grid>
                </Grid>
            </Box>
            <Box>
                <Grid container justifyContent={"center"}>
                    <Grid item xs={4} sx={{mr:1, mb:2}}>
                        <TextField label="WAGER"/>
                    </Grid>
                    <Grid item xs={4} sx={{ml:1, mb:2}}>
                        <TextField label="TO WIN"/>
                    </Grid>
                </Grid>
            </Box>
        </Box>
    )
 }
