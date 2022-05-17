import React, { Component, useState, useEffect } from "react";
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
    const [selectedBets, setSelectedBets] = useState(props.data)

    useEffect(() => {
        setSelectedBets(props.data)
    }, [props.data])

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
                    {selectedBets.map((bet, index) =>
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