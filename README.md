# smallcloud
AI-powered, AWS-services–focused cloud cost governor

## Purpose

When working with cloud services like AWS:
common to have resources you don’t need
end up paying way too much for

Leverage AI to monitor cloud spend and make decisions to reduce the cloud 
resources without affecting app functionalities.

## Problem

Existing solutions are difficult to read + understand: 
sifting through CloudWatch logs
navigating to Billings and Cost Management tabs
persons interested in cost may not understand the importance of a given cloud offering.

## Design Principles

AI cannot add/remove cloud resources without human approval (HITL)
Every recommendation AI makes must cite evidence
Every action needs to be able to be rolled-back by one-click.
PRs, API writes
Projected vs. realized savings

## Stack

TypeScript (API)
Next.js dashboard
Python, FastAPI (Agent + analytics)
Data stores (Postgres)
Execution (Terraform PRs, API calls)
