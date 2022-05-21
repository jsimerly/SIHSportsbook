import React, { Component, useState, useEffect } from "react";
import {
    Grid,
    List,
    Button,
    Box,
    IconButton,
    Icon,
    Typography
 } from '@mui/material';
 import DeleteForeverIcon from '@mui/icons-material/DeleteForever';
 import CachedIcon from '@mui/icons-material/Cached';

 import BetSlipTile from "../molecules/BetSlipTile";
 import ParlayTile from "../molecules/ParlayTile";

export default function BetSlip(props){
    const [selectedBets, setSelectedBets] = useState(props.selectedBets)
    const [parlayStatus, setParlayStatus] = useState(true)

    useEffect(() => {
        setSelectedBets(props.data)
    }, [props.data])

    function submitButton() {
        if (props.selectedBets.length === 0 ){
            return (<div></div>)
        } else {
            return (<Button> Submit Bet </Button>)
        }
    }

    function handleParlayToggle() {
        setParlayStatus(!parlayStatus)
    }

    function parlayButton() {
        console.log(parlayStatus)
        if (parlayStatus) {
            return (
                <IconButton onClick={handleParlayToggle} sx={{borderRadius: 0}}>
                    <CachedIcon sx={{fontSize: 18, mr:1}}/> <Typography> Parlay </Typography>
                </IconButton>
            )
        } else {
            return(
                <IconButton onClick={handleParlayToggle} sx={{borderRadius: 0}}>
                    <CachedIcon sx={{fontSize: 18, mr:1 }}/> <Typography> Straight </Typography>
                </IconButton>
            )
        }
    }

    function parlayToggleComponent(){
        if (parlayStatus) {
            return (
                <ParlayTile 
                    selectedBets={props.selectedBets}
                    handleRemoveBet={props.handleRemoveBet}
                />
            )
        } else {
            return (
                <List>
                    {props.selectedBets.map((bet, index) =>
                        <BetSlipTile 
                            bet={bet}
                            handleRemoveBet={props.handleRemoveBet}
                        />
                    )}
                </List>
            )
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
                       {parlayButton()}
                    </Grid>
                    <Grid item xs={2}>
                        <IconButton onClick={props.handleRemoveAllBets}>
                            <DeleteForeverIcon/>
                        </IconButton>
                    </Grid>
                </Grid>
                {parlayToggleComponent()}
                {submitButton()}
            </Box>
    )
}