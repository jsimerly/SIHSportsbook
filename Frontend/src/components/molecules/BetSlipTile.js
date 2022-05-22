import React, { Component, useState } from "react";
import { 
    Grid,
    Box,
    TextField,
    IconButton,
} from "@mui/material";
import RemoveCircleOutlineIcon from '@mui/icons-material/RemoveCircleOutline';

export default function BetSlipTile(props){
    function handleRemoveBet() {
        props.handleRemoveBet(props.bet)
    }

    return (
        <Box sx={{border:1}}>
            <Box sx={{p:1}}>
                <Grid container>
                    <Grid item xs={1}>
                        <IconButton onClick={handleRemoveBet}>
                            <RemoveCircleOutlineIcon sx={{fontSize: 10}}/>
                        </IconButton>
                    </Grid>
                    <Grid item xs={11}>
                        <Box>
                            <Grid container>
                                <Grid item xs={9}>
                                    {props.bet.vanity.main}
                                </Grid>
                                <Grid item xs={3}>
                                    {props.bet.vanity.line}
                                </Grid>
                            </Grid>
                        </Box>
                        <Box>
                            {props.bet.vanity.secondary}
                        </Box>
                        <Box sx={{fontSize:10}}>
                            <Grid container>
                                <Grid item xs={9}>
                                    {props.bet.matchupData.data.team1} @ {props.bet.matchupData.data.team2}
                                </Grid>
                                <Grid item xs={3}>
                                    {props.bet.matchupData.payoutDate}
                                </Grid>
                            </Grid>
                        </Box>
                    </Grid>
                </Grid>
            </Box>
            <Box>
                <Grid container justifyContent={"center"}>
                    <Grid item xs={4} sx={{mr:1, mb:2}}>
                        <TextField size="small" label="WAGER"/>
                    </Grid>
                    <Grid item xs={4} sx={{ml:1, mb:2}}>
                        <TextField size="small" label="TO WIN"/>
                    </Grid>
                </Grid>
            </Box>
        </Box>
    )
 }
