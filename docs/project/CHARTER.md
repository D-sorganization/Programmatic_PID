# Project Charter

> Drafted 2026-09-25 by the fleet charter sweep (Gemini) from README, git history, and open issues/PRs.
> The project-steward role keeps this current; owners should correct feature statuses.

## End Goal

Programmatic-PID provides a declarative Python framework and CLI tool for generating standard-compliant, editable Piping and Instrumentation Diagrams (P&IDs) in DXF and SVG formats directly from YAML specifications. "Done" looks like a stable, fully typed, and verified drawing compilation engine capable of rendering multi-sheet process and control diagrams—including automated stream routing, equipment symbols, instrument bubbles, and control loops—without requiring manual CAD drafting for initial engineering reviews.

## Non-Goals

- Interactive GUI-based CAD drawing or diagram authoring (YAML is the sole source of truth).
- Replacement for full-featured CAD suites (e.g. AutoCAD, SolidWorks) beyond initial drafting and review generation.
- Dynamic physical process simulation, hydraulic calculation, or automated mass/energy balance solving.
- Proprietary or binary CAD file format generation beyond standard DXF (ezdxf) and SVG previews.

## Features

| ID | Feature | Status | Tracking | Notes |
| --- | --- | --- | --- | --- |
| F1 | Declarative YAML Spec Parsing and Validation | shipped | #51 | Validates YAML specs with strict dimension types and SpecValidationError |
| F2 | JSON Schema Spec Autocompletion | shipped | - | Schema for real-time editor autocompletion and structural validation |
| F3 | Equipment Symbols Library | shipped | #40 | Renders standard symbols for vessels, hoppers, fans, and valves |
| F4 | Process Stream Routing | shipped | #50 | Computes polyline routes with arrowheads and collision avoidance |
| F5 | Instrument Tag and Leader Placement | shipped | #18 | Renders bubble tags and leader lines with position spreading |
| F6 | Control Loop Signal Routing | shipped | #67 | Draws signal lines from measurement transmitters to final elements |
| F7 | Engineering Annotation Panels | shipped | #38 | Renders title blocks, notes, control summaries, and mass balances |
| F8 | Multi-Sheet Output Architecture | shipped | #30 | Generates separate process and control/interlock sheets from one spec |
| F9 | Modular DXF CAD Generation Engine | shipped | #58 | Emits editable DXF drawings via decomposed geometry and layer submodules |
| F10 | SVG Drawing Preview Export | shipped | #78 | Produces vector SVG previews with fallback error handling |
| F11 | Configurable Layout Profiles | shipped | - | Applies presentation, review, and compact layout overlay configurations |
| F12 | CLI Drawing Generator | shipped | #37 | Provides generate-pid command-line interface for drafting workflows |
| F13 | C4 Architecture Contract | shipped | - | Visual C4 architecture map validated by automated CI contract script |
| F14 | Geometric Performance Benchmarks | shipped | #79 | Tracks DXF helper execution speed with pytest-benchmark |

## Links

- Status (generated): [`STATUS.md`](STATUS.md)
- Steward playbook: Repository_Management `docs/fleet-project-steward.md`
