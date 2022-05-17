import React, { Component, useState } from "react";
import { render } from "react-dom";
import DrawerComp from "../organisms/Drawer";
import Matchups from "../organisms/Matchups";
import MatchUp from "../molecules/MatchUp";
import BetSlip from "../organisms/BetSlip";
import {
    Box,
    Grid
} from '@mui/material'


export default function App(props){
    const [selectedBets, setSelectedBets] = useState([])

    const matchupsJson = [
        {   id: 1,
            matchupId: 1,
            payoutDate: "Tues 3:00 AM",
            vig: 0.05,
            data: { 
                team1: "Sugma",
                team2: "'Member Berries",
                over: "220",
                under: "220",
                sp_pos: "+3.5",
                sp_neg: "-3.5",
                ml_pos: +210,
                ml_neg: -180
            },
        },
        {   id: 2,
            matchupId: 1,
            payoutDate: "Tues 3:00 AM",
            vig: 0.05,
            data: { 
                team1: "Team 3",
                team2: "Team 4",
                over: "120",
                under: "120",
                sp_pos: "+5.5",
                sp_neg: "-5.5",
                ml_pos: 115,
                ml_neg: -129,
            }
        },
        {   id: 3,
            matchupId: 1,
            payoutDate: "Tues 3:00 AM",
            vig: 0.05,
            data: { 
                team1: "Team 5",
                team2: "Team 6",
                over: "120",
                under: "120",
                sp_pos: "+5.5",
                sp_neg: "-5.5",
                ml_pos: 115,
                ml_neg: -129
            }
        },
    ]

    function handleBetSelected(newBetList) {
        // const betType = newBet.betData.betType
        // const betValue = newBet.matchupData.data[betType]
     
        setSelectedBets(newBetList)
        console.log(selectedBets)
    }

    return (
        <div>
            <Grid container>
                <Grid item>
                    <Box sx={{width: 250, height: '100vh', border:1 }}>
                        <DrawerComp/>
                    </Box>
                </Grid>
                <Grid margin={2} md={7} spacing={1} sx={{border:1}}>
                    <Matchups data={matchupsJson} betHandler={handleBetSelected}/>
                </Grid>
                <Grid margin={2} md={2} spacing={1} sx={{border:1}}>
                    <BetSlip data={selectedBets}/>
                </Grid>
            </Grid>
        </div>
    )
}