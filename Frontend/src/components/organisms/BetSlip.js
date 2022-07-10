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

 import BetSlipTiles from "../molecules/BetSlipTiles";
 import ParlayTile from "../molecules/ParlayTile";
 import SubmitBetButton from "../molecules/SubmitBetButton";

export default function BetSlip(props){
    const [parlayStatus, setParlayStatus] = useState(false)

    function submitButtonIf() {
        if (props.selectedBets.length === 0 ){
            return (<div></div>)
        } else {
            return (<SubmitBetButton handleButtonClicked={props.handleSubmitBets}/>)
        }
    }

    function handleParlayToggle() {
        setParlayStatus(!parlayStatus)
        props.handleParlayStatus(!parlayStatus)
    }

    function parlayButton() {
        
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
                    parlayWager={props.parlayWager}
                    selectedBets={props.selectedBets}
                    handleRemoveBet={props.handleRemoveBet}
                    handleWager={props.handleParlayWager}
                    handleParlayReady={props.handleParlayReady}    
                    parlayVig = {props.parlayVig} 
                />
            )
        } else {
            return (
                <BetSlipTiles
                    selectedBets={props.selectedBets}
                    handleRemoveBet={props.handleRemoveBet}
                    handleWager={props.handleWager}
                />
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
                {submitButtonIf()}
            </Box>
    )
}