import React, { Component, useState } from "react";
import { 
    Grid,
    Box,
    Divider,
    ToggleButtonGroup
} from "@mui/material";
import MatchUp from "../molecules/MatchUp";

export default function Matchups(props){
    const matchupsJson = props.data
    const [betList, setBetList] = useState([])

    function checkDupsIndex(betArray, newBet) {
        for (var i = 0; i < betArray.length; i++) {
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

    function handleBetSelected(matchupData, betType, team) {
        const betValue = matchupData.data[betType]
        const newBet = {
            matchupData,
            betData : {
                betType: betType,
                betValue: betValue,
                team: team,
            }
        }
        let newBetList = betList
        const dupIndex = checkDupsIndex(newBetList, newBet)

        if (dupIndex != -1) {
            newBetList.splice(dupIndex, 1)
        } else {
            newBetList.push(newBet)
        }
        props.betHandler(newBetList)
    }

    const matchupsDiv = (  
        <Box> 
            <ToggleButtonGroup
                onChange = {handleBetSelected}
                fullWidth="true"
                orientation="vertical"
            >            
            {matchupsJson.map((matchupJson, index) => {
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
  