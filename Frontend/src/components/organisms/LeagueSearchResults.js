import React, { Component, useState, useEffect } from "react";
import {
    Grid,
    Box,
    IconButton,
    Typography
 } from '@mui/material';
 import DeleteForeverIcon from '@mui/icons-material/DeleteForever';
 import CachedIcon from '@mui/icons-material/Cached';

 import BetSlipTiles from "../molecules/BetSlipTiles";
 import ParlayTile from "../molecules/ParlayTile";
 import SubmitBetButton from "../molecules/SubmitBetButton";

export default function LeagueSearchResults(props){
    const [leagues, setLeagues] = useState({
        'league_name' : 'None'
    })

    useEffect(() => {
        setLeagues(props.leagues);
    }, [props.leagues])

    function submitButtonIf() {
        if (props.selectedBets.length === 0 ){
            return (<div></div>)
        } else {
            return (<SubmitBetButton handleButtonClicked={props.handleSubmitBets}/>)
        }
    }
    
    console.log('----------')
    console.log(props.leagues)

    return (
            <Box sx={{
                display: 'flex',
                alignItems: 'center',
                flexDirection: 'column',
                borderRadius: 1,
                }}
            >
                Leagues
                {leagues.league_name}
            </Box>
    )
}