import React, { Component, useState, useEffect } from "react";
import {
    Grid,
    Box,
    IconButton,
    Typography,
    List,
    ListItem,
    Button,
 } from '@mui/material';

import SearchLeagueSingleResult from "../molecules/SearchLeagueSingleResult";

export default function SearchLeagueResults(props){
    const [leagues, setLeagues] = useState({
        'league_name' : 'None'
    })
    const csrftoken = props.getCookie('csrftoken')

    useEffect(() => {
        setLeagues(props.leagues);
    }, [props.leagues])


    return (
        <Grid
            item
            sx={{
                display: 'flex',
                alignItems: 'center',
                flexDirection: 'column',
                borderRadius: 1,
                }}
            container
        >
            <Grid item >
                <Box>
                    <Typography component='h5' variant='h5'>
                        Fantasy League
                    </Typography>
                </Box>
                <Box>
                    {console.log(leagues)}
                    <SearchLeagueSingleResult 
                        league_label = {leagues.league_name}
                        league_id = {leagues.league_id}
                        button_type='create'
                        getCookie = {props.getCookie}
                    />
                </Box>
                <Box>
                    <Typography component='h5' variant='h5'>
                        Active Betting Leagues
                    </Typography>
                </Box>
                <Box>
                    {leagues.betting_leagues?.map((betting_league, index)=>{
                        return (
                            <Box>
                                <SearchLeagueSingleResult 
                                    league_label = {betting_league.league_name}
                                    league_id = {betting_league.league_id}
                                    button_type='join'
                                    getCookie = {props.getCookie}
                                />
                            </Box>
                        )
                    })}
                </Box>
            </Grid>
        </Grid>

    )
}