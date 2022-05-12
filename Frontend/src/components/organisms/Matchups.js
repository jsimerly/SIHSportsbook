import React, { Component, useState } from "react";
import { 
    Grid,
    Box,
    Divider,
    ToggleButtonGroup
} from "@mui/material";
import MatchUp from "../molecules/MatchUp";

export default function Matchups(props){
    const matchupsJson = [
        {
        id: 1,
        data: { 
            team1: "Team 1",
            team2: "Team 2",
            over: "220",
            under: "220",
            sp_pos: "+3.5",
            sp_neg: "-3.5",
            ml_pos: +210,
            ml_neg: -180
        }},
        {
        id: 2,    
        data: { 
            team1: "Team 3",
            team2: "Team 4",
            over: "120",
            under: "120",
            sp_pos: "+5.5",
            sp_neg: "-5.5",
            ml_pos: 115,
            ml_neg: -129,
        }},
        {
        id: 3,    
        data: { 
            team1: "Team 5",
            team2: "Team 6",
            over: "120",
            under: "120",
            sp_pos: "+5.5",
            sp_neg: "-5.5",
            ml_pos: 115,
            ml_neg: -129
        }},
    ]

    const [matchups, setMatchups] = useState(matchupsJson);
    let betList = []
    const [bets, setBets] = useState(betList);

    function addBet(newBet) {
        const currentBets = bets;
        setBets({currentBets: [...currentBets, + newBet]});
    }

    function removeBet(newBet) {
        const currentBets = bets;
        if (currentBets.length > 0){
            setBets(currentBets.filter(newBet))
        }
    }

    function handleBetSelected(id, betType) {
        const newBet = [id, betType]
        console.log("new Bet: " + newBet)

        if (betList.includes(newBet)) {
            console.log("FOUND DUPLICATE")
        } else {
            console.log("not found")
        }

        betList.push(newBet)
        console.log("betList: " + betList)
    }

    const matchupsDiv = (
        <Box> 
            <ToggleButtonGroup
                value={bets}
                onChange = {handleBetSelected}
                fullWidth="true"
                orientation="vertical"
            >            
            {matchups.map((matchupJson, index) => {
                const matchupData = matchupJson
                return (
                   <MatchUp 
                        matchupData={matchupData}
                        betHandler={handleBetSelected}
                    />
                )
            })}
            </ToggleButtonGroup>
        </Box>
   )
   
    return (
        <div>{matchupsDiv}</div>
    )
}
  