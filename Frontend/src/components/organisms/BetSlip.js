import React, { Component } from "react";
import {
    Grid,
    List,
    ListItem,
    Button,
    TextField,
    Box
 } from '@mui/material';
 import BetSlipTile from "../molecules/BetSlipTile";

export default function BetSlip(props){
    return (
            <Box sx={{
                display: 'flex',
                alignItems: 'center',
                flexDirection: 'column',
                borderRadius: 1,
                }}
            >
                <Grid container sx={{border:1, p:1, mb:1}}>
                    <Grid item xs={10}>
                       2 -  Betslip
                    </Grid>
                    <Grid item xs={2}>
                        Parlay
                    </Grid>
                </Grid>
                <List>
                    {['Over 230', 'Under 220'].map((bet, index) =>
                        <BetSlipTile betData={bet}/>
                    )}
                </List>
                <Box sx={{border:1, width:'100%'}}>
                    <Box>
                        Remove All
                    </Box>
                </Box>
                <Button>
                    Place Bet
                </Button>
            </Box>
    )
}