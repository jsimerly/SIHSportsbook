import React, { Component, useState, useEffect } from "react";
import {
    Grid,
    List,
    Button,
    Box,
    IconButton,
    Icon,
 } from '@mui/material';
 import BetSlipTile from "../molecules/BetSlipTile";
 import DeleteForeverIcon from '@mui/icons-material/DeleteForever';

export default function BetSlip(props){
    const [selectedBets, setSelectedBets] = useState(props.data)

    useEffect(() => {
        setSelectedBets(props.data)
    }, [props.data])

    function submitButton() {
        if (selectedBets.length === 0 ){
            console.log('empty')
            return (<div></div>)
        } else {
            return (<Button> Submit Bet </Button>)
        }
    }

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
                       {selectedBets.length} -  Betslip
                    </Grid>
                    <Grid item xs={2}>
                        <IconButton onClick={props.handleRemoveAllBets}>
                            <DeleteForeverIcon/>
                        </IconButton>
                    </Grid>
                </Grid>
                <List>
                    {selectedBets.map((bet, index) =>
                        <BetSlipTile 
                            bet={bet}
                            handleRemoveBet={props.handleRemoveBet}
                        />
                    )}
                </List>
                {submitButton()}
            </Box>
    )
}