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

    const [selectedBets, setSelectedBets] = useState([]);

    function checkDupsIndex(betArray, newBet) {
        for (var i=0; i < betArray.length; i++) {
            const betId = betArray[i].matchupData.id
            const newBetId = newBet.matchupData.id
            const betType = betArray[i].betData.betType
            const newBetType = newBet.betData.betType

            if (betId == newBetId && betType == newBetType) {
                return i
            }
        }
        return -1
    }

    function betSelectedHandler(newBet) {
        let newBetArr = selectedBets;
        const dupIndex = checkDupsIndex(newBetArr, newBet)

        if (dupIndex != -1) {
            newBetArr.splice(dupIndex,1)
        } else {
            newBetArr.push(newBet)
        }
        setSelectedBets([...newBetArr])
        console.log(selectedBets)
    }

    function handleRemoveBet(removedBet) {
        const dupIndex = checkDupsIndex(selectedBets, removedBet)
        setSelectedBets([
            ...selectedBets.slice(0, dupIndex),
            ...selectedBets.slice(dupIndex + 1)
        ])
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
                    <Matchups 
                        data={matchupsJson} 
                        betSelectedHandler={betSelectedHandler}
                        selectedBets={selectedBets}
                        checkDupsIndex={checkDupsIndex}
                    />
                </Grid>
                {/* <Grid margin={2} md={2} spacing={1} sx={{border:1}}>
                    <BetSlip removeHandler={handle} data={selectedBets}/>
                </Grid> */}
            </Grid>
        </div>
    )
}