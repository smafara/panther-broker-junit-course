# Unit testing a fractional investing simulator

Research and course design: 31 October 2026. Intended stack: JDK 25, JUnit Jupiter 6, Mockito 5, Maven. Video-only course with optional, ungraded practice. Working project name: **Fracción**.

## Research that changes the project

Fintual Acciones Mexico currently advertises complete and fractional US shares and ETFs from USD 1, zero trading or administration commission, and a 0.5% FX spread. These are the terms of Acciones, not the fees of its managed investment funds. [Fintual Acciones](https://fintual.mx/acciones/)

GBM Trading USA offers complete and fractional US instruments and currently lists 0.25% commission for purchases and sales. Its minimum-investment FAQ describes entry from MXN 100; that wording does not establish a universal minimum for every individual order. [Product](https://gbm.com/faqs/que-es-trading-usa), [commission](https://gbm.com/faqs/existe-alguna-comision-por-invertir-en-trading-usa/), [minimum](https://gbm.com/faqs/cual-es-el-monto-minimo-para-invertir/)

GBM's current help center describes a USD-denominated Trading USA experience, funded through Smart Cash with an explicit currency conversion. This is a useful architectural distinction: currency conversion and security execution are separate operations. [GBM help center](https://gbm.com/faqs)

The simulator borrows that workflow, but its rules below are explicitly course rules. They do not reproduce either company's complete execution, rounding, fee, or settlement behavior.

NYSE regular trading is 09:30–16:00 Eastern Time, with holidays and early closes. A fixed Mexico City window is incorrect for a US-equity calendar. Platform operating windows can also differ from exchange hours. [NYSE calendar](https://www.nyse.com/markets/hours-calendars)

Six fractional decimal places are a course choice. For comparison, Alpaca documents up to nine decimal places in fractional order quantity and notional fields; this does not establish the precision exposed by Fintual's application. [Alpaca fractional trading](https://docs.alpaca.markets/us/docs/fractional-trading)

## Council decision

Keep the investing narrative and a single evolving repository. Reduce the financial surface area to funding, FX conversion, previews, buys, and partial/full sales. Introduce no database, HTTP implementation, frontend, or account-opening flow.

The teaching priority is expressing a behavior as a test, understanding failure, and changing code safely. Remove tax withholding, SAT submissions, FIFO tax lots, wash-sale detection, margin, KYC, RFC/CLABE algorithms, SPEI, dividends, stop-losses, and robo-advisory allocation from the core course. They each need additional domain explanation without improving the basic JUnit lesson.

Use quote freshness for the core Clock lesson. Exchange calendars are an optional extension. Keep test ordering out of the core: every test must run independently. Teach explicit constructor wiring before showing @InjectMocks as an optional shorthand.

## Audience and completion outcomes

Prerequisites: Java methods, classes, constructors, interfaces, exceptions, collections, and basic Maven use. Supply a short primer on records and BigDecimal. Advanced Java syntax is not a learning objective.

By the end, viewers can write and diagnose Jupiter tests, select meaningful examples and boundaries, isolate mutable fixtures, test exceptions and unchanged state, parameterize repeated cases, substitute external dependencies, verify meaningful side effects, control time, perform small TDD cycles, and refactor with characterization tests.

## The course's explicit business contract

1. Funding adds positive MXN to an in-memory wallet. Conversion consumes MXN and credits USD; both balances remain visible.
2. An FX quote expresses **MXN per USD**. The demo conversion policy computes an offered rate as reference rate × (1 + spread), then divides MXN by that rate. This is a transparent teaching formula, not an assertion about either broker's implementation.
3. Currency credits and debits use two decimal places. Conversion credits round DOWN so they cannot create spending power. Rounding residue stays visible in the conversion receipt; it is not silently represented as spendable cash.
4. A buy request's notional USD is the security amount, excluding commission. Quantity = notional / USD unit price, rounded DOWN to six decimal places. Actual gross = quantity × price, rounded to cents with HALF_EVEN. Fee = actual gross × configured rate, rounded to cents with HALF_EVEN. Debit = gross + fee. Unused funds stay in cash.
5. The fictional fee policy offers ZERO = 0% and STANDARD = 0.25%. These are isolated teaching fixtures, not a combined Fintual/GBM tariff. The base simulator omits taxes.
6. Sales accept a positive quantity with at most six decimal places, cannot exceed holdings, and credit gross minus fee. The same gross and fee rounding rules apply.
7. Invalid requests throw a validation exception. Expected execution failures return a result with a reason, such as insufficient cash or missing quote. Rejected operations leave cash and holdings unchanged and emit no completed-trade event.
8. The broker simulates one immediate full fill at the supplied quote. It does not model partial fills, market liquidity, pending orders, or settlement. A preview is an estimate, not a real-world execution guarantee.
9. Quotes contain ticker, USD price, and an Instant. Price must be positive. In the time lesson, age less than 30 seconds is fresh; age exactly 30 seconds is stale; future-dated quotes are rejected.

BigDecimal must be constructed from decimal strings for the examples. Its equals compares value and scale; compareTo provides numerical comparison. Choose the assertion according to whether scale is part of the contract. [JDK 25 BigDecimal](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/math/BigDecimal.html)

Worked buy: USD cash 50.00, notional 40.00, price 125.00, STANDARD fee. Quantity = 0.320000, gross = 40.00, fee = 0.10, debit = 40.10, cash remaining = 9.90. If cash is only 40.00, reject with no mutation. Do not reuse the draft's 0.400000-share example while also silently charging a commission from the same USD 50 budget.

## Small architecture

- Pure calculation: FractionalCalculator and FeePolicy.
- Values: Quote, TradeRequest, TradePreview, TradeReceipt, and ExecutionResult.
- Mutable state: PortfolioWallet with MXN, USD, and ticker quantities.
- Coordination: TradeService.
- Boundaries introduced gradually: FxQuoteProvider, QuoteProvider, TradeEventPublisher, and java.time.Clock.

Use an in-memory wallet directly in service tests. There is no need to mock every object. Add records and enums as needed without pretending that eight total types can contain the entire original financial syllabus.

## Granular video coursework

Each episode starts with a behavior card, asks viewers to predict one outcome, demonstrates a meaningful failure, implements or repairs behavior, and ends with a small optional challenge. The listed durations include explanation and reading test output.

### 1.1 — A calculation printed correctly can still be wrong (9 minutes)

**Outcome:** Distinguish observation from automated verification.

**Timeline:** 0–2: show an existing fractional purchase preview and write the expected debit; 2–4: use the reproducible 0.1 + 0.2 floating-point example; 4–6: show a commission percentage defect that looks plausible in console output; 6–8: introduce BigDecimal strings and the course's monetary contract; 8–9: recap expected versus actual.

**Artifact:** A tiny manual preview runner plus a prepared FractionalCalculator skeleton. Keep the runner in history rather than implying main methods are inherently bad.

**Challenge:** For three supplied preview inputs, write expected quantity, fee, and debit. Success means explaining which value would reveal a percentage bug. No unseen JUnit APIs required.

### 1.2 — First Jupiter test and a useful red bar (15 minutes)

**Outcome:** Run one test from both IDE and Maven and interpret its failure.

**Timeline:** 0–3: inspect JDK and Maven versions and the prepared POM; 3–5: explain src/main/java versus src/test/java and Jupiter; 5–9: write calculatesFractionalQuantity using @Test and Arrange–Act–Assert; 9–12: deliberately change the divisor or rounding and read expected/actual plus stack location; 12–14: repair and run ./mvnw test; 14–15: challenge.

**Examples:** 40.00 / 125.00 = 0.320000; 10.00 / 3.00 = 3.333333.

**Challenge:** Test exact division and a repeating fraction. Check six-decimal output explicitly. Keep zero/negative validation for module 2.

### 1.3 — Receipt assertions, equality, and assertAll (12 minutes)

**Outcome:** Assert a complete observable result without hiding secondary failures.

**Flow:** Compare 0.32 with 0.320000 and explain scale; use exact equality for canonical quantities and compareTo for value-only checks; test the worked receipt above; break fee and remaining cash; group independent checks with assertAll; show one useful lazy failure message.

**Challenge:** Add a non-exact division preview and assert quantity, gross, commission, debit, and remaining cash. Values come from the contract, not by copying the implementation formula into the test.

### 2.1 — Wallet fixtures and independent tests (11 minutes)

**Outcome:** Understand per-method instances and safe mutable setup.

**Flow:** Write deposit and debit tests with repeated construction; extract a fresh wallet into @BeforeEach; show that one test's debit does not affect another; contrast a static shared wallet; briefly demonstrate @BeforeAll for immutable setup and @AfterEach for cleanup when actually needed.

**Challenge:** Repair a supplied shared-wallet test class. It must pass when run individually and as a whole, without relying on method order.

### 2.2 — Reject the order without damaging the wallet (12 minutes)

**Outcome:** Test exception information and invariants after failure.

**Flow:** Test zero and negative deposit amounts with assertThrows; capture an InsufficientHoldingsException; inspect ticker and shortfall; attempt to sell 0.500000 when holdings are 0.400000; assert both shares and cash are unchanged; distinguish programmer/input errors from expected execution rejection results.

**Challenge:** Test over-selling and a negative buy amount. Verify unchanged state as well as the exception or rejection. Include the valid boundary: selling exactly the full holding.

### 2.3 — Readable wallet scenarios with @Nested (10 minutes)

**Outcome:** Organize tests around meaningful states.

**Flow:** Reorganize familiar tests into WhenEmpty, WhenFunded, and WhenHoldingShares; explain outer-to-inner @BeforeEach setup; add readable @DisplayName labels; show @Disabled with a reason and explain that skipped tests provide no passing evidence.

**Challenge:** Reorganize the existing sell tests into partial-sale and full-liquidation scenarios. Preserve behavior and independent execution.

### 3.1 — Replace repeated validation tests with data (10 minutes)

**Outcome:** Use @ParameterizedTest, @ValueSource, and @NullAndEmptySource.

**Flow:** Collapse repeated ticker-input tests. The teaching rule is deliberately narrow: a non-null, nonblank identifier from a supplied supported-instrument catalog. Do not claim a regex proves exchange listing. Separate blank-input rejection from unsupported-symbol rejection; inspect each generated test invocation.

**Challenge:** Parameterize null, empty, blank, and unsupported ticker cases. Add a supported symbol case using only APIs already shown.

### 3.2 — Fee rules as executable tables (12 minutes)

**Outcome:** Express input/output examples and boundaries in @CsvSource.

**Flow:** Introduce enum conversion and BigDecimal parameters; write a text-block table for ZERO/STANDARD fees; include zero fee, ordinary amounts, and half-cent rounding boundaries; explain explicit expected literals; use headers to clarify runner output. If time permits, show @EnumSource for a property shared by all supported order sides.

**Table seeds:** STANDARD, 40.00, 0.10; STANDARD, 1.00, 0.00; STANDARD, 2.00, 0.00; STANDARD, 6.00, 0.02; ZERO, 40.00, 0.00. The 2.00 and 6.00 cases expose HALF_EVEN ties at 0.005 and 0.015.

**Challenge:** Add immediately adjacent values around one rounding boundary and explain why one expected fee changes.

### 3.3 — Whole portfolio scenarios with @MethodSource (12 minutes)

**Outcome:** Supply complex, independently created fixtures.

**Flow:** Create Stream<Arguments> for partial sale, full liquidation, and insufficient holdings; label cases with Named; ensure each case owns a fresh mutable wallet; assert receipt and resulting state. Explain why a nested object graph is clearer in Java than CSV.

**Challenge:** Add a second ticker and prove selling the first leaves the second unchanged. Do not introduce rebalancing algorithms.

### 4.1 — Dependency seams before Mockito (14 minutes)

**Outcome:** Make external values controllable through constructor injection.

**Flow:** Show a changing quote making expected results unstable; extract QuoteProvider; implement a tiny handwritten stub returning a fixed Quote; wire it manually into TradeService; identify pure calculations versus external boundaries; add Mockito dependencies and explain the startup-agent setup once.

**Challenge:** Replace a hardcoded FX lookup with an injected FxQuoteProvider and a fixed stub. No real HTTP request is needed.

### 4.2 — Mockito stubbing and execution results (14 minutes)

**Outcome:** Use MockitoExtension, @Mock, when/thenReturn, and when/thenThrow.

**Flow:** Construct TradeService explicitly with a mocked provider and real wallet; stub a 125.00 quote; buy 40.00 with 50.00 cash; assert a filled receipt and 9.90 remaining; test missing quote and provider exception; show an argument mismatch or unused stubbing diagnostic without claiming every mismatch is detected immediately in every context.

**Challenge:** Add a provider failure case and prove no balance or holding changed. Optionally compare explicit construction with @InjectMocks after dependencies are understood.

### 4.3 — Verify a completed-trade event (12 minutes)

**Outcome:** Verify externally observable collaboration.

**Flow:** Inject TradeEventPublisher; verify one completed event after a successful trade; capture its TradeReceipt with ArgumentCaptor; assert ticker, side, quantity, and debit; verify no completed event for a rejected trade. Prefer state assertions for wallet outcomes and interaction assertions for publication.

**Challenge:** Capture a partial-sale receipt and check quantity and net proceeds. Avoid verifying every private implementation step.

### 5.1 — TDD a purchase limit (15 minutes)

**Outcome:** Complete three small red–green–refactor cycles.

**Feature card:** Reject a buy whose security notional exceeds the account's configured per-order limit; equality is allowed; sells are unaffected.

**Flow:** Cycle 1 allows below-limit purchase; cycle 2 rejects above-limit purchase; cycle 3 accepts exact equality; refactor duplicated comparisons while the suite stays green. Start with the smallest useful example rather than introducing an allocation engine.

**Challenge:** Add the sell exemption and a test proving a rejected buy preserves balances. State the expected behavior before writing production code.

### 5.2 — Quote freshness with java.time.Clock (14 minutes)

**Outcome:** Control time and test exact boundaries.

**Flow:** Replace Instant.now() with an injected Clock; use Clock.fixed; test ages 29 seconds, exactly 30 seconds, and 31 seconds; reject future quotes; deliberately replace < with <= and show which assertion catches it. Use this defect to explain why executing a line does not prove its behavior is correct. A coverage report is optional and requires a separately verified JDK-25-compatible tool version.

**Challenge:** Add subsecond examples immediately before and at expiration. Run the tests at any wall-clock time with the same results.

### 5.3 — Characterize and refactor the broker you already know (18 minutes)

**Outcome:** Separate structural refactoring from behavior change.

**Flow:** Use a messy version of the familiar preview method; characterize exact division, repeating fractions, fee rounding, insufficient funds, partial sale, and full sale; inspect observed outputs and compare them with the written contract; extract calculation and validation helpers; run tests after each small change. If an observed legacy behavior contradicts the contract, label it explicitly, then fix it in a separate change with a targeted regression test.

**Challenge:** Refactor a second familiar method while keeping the suite green. Supply an optional solution recording explaining each change.

## Optional extension videos

1. Market sessions: inject a calendar alongside Clock; use America/New_York, opening/closing boundaries, winter/summer offsets, a US holiday, and an early close. An out-of-session result in this simulator is its own policy, not a claim about platform order queuing.
2. Mutation testing: demonstrate a meaningful surviving mutation and improve an assertion.
3. Integration versus unit tests: contract-test a local fake HTTP quote server separately from the pure unit suite.

## Recording and repository conventions

The main sequence is approximately 190 minutes. Budget more time for setup and refactoring than for individual annotations. Avoid typing complete domain boilerplate on camera.

For every episode provide immutable tags such as ep-1.2-start, ep-1.2-end, and ep-1.2-solution. Every end tag passes the complete suite. Mark intentionally failing demonstrations explicitly. Challenges have their own short acceptance checklist and solutions; no grading or submission requirement.

Provide a Spanish README and recording script if the institutional audience is Spanish-speaking; keep ordinary Java identifiers consistent. Include the Maven wrapper, pinned dependencies, instructions for IDE and terminal, and the exact JDK used to record. Explain that the course can be followed by watching, with coding along optional.

## Stack status and verification boundary

The current official JUnit guide resolves to **6.1.3**; use the 6.1.3 BOM and junit-jupiter rather than calling 6.1.0 the latest. Mockito's official latest release is **5.24.0**. [JUnit](https://docs.junit.org/6.1.3/overview.html), [Mockito](https://github.com/mockito/mockito/releases/tag/v5.24.0)

Retain JDK 25 as requested. Use supported stable Java features without preview flags. Teach testing rather than an inventory of new language features. Version discovery is research, not proof that a project builds: this document does not include a scaffold and no Maven build has been run.

Before recording, compile the final repository with JDK 25, run the full suite through its wrapper, confirm Mockito's startup-agent configuration in both Maven and the chosen IDE runner, and freeze the working versions. Keep build troubleshooting out of each subsequent episode.

Use Surefire **3.6.1**, the current stable release identified in the [Apache releases](https://github.com/apache/maven-surefire/releases). Follow [Mockito's Java 21+ instrumentation instructions](https://javadoc.io/static/org.mockito/mockito-core/5.24.0/org.mockito/org/mockito/Mockito.html#0.3): resolve the agent using Maven dependency properties rather than constructing a local-repository path. Preserve Surefire's late argLine replacement if later adding a coverage agent. This configuration issue begins with Java 21+, not only Java 25.

## Corrections to retain in the recording notes

- CSV text blocks and hash-prefixed comment lines predate JUnit 6; do not credit them to the FastCSV migration. Describe comment lines rather than promising arbitrary trailing inline comments. [JUnit 5 CsvSource API](https://docs.junit.org/5.13.4/api/org.junit.jupiter.params/org/junit/jupiter/params/provider/CsvSource.html)
- Unified versions, inherited nested method ordering, FastCSV, and ConsoleLauncher fail-fast belong to the JUnit 6.0 changes. They are not all 6.1 additions. ConsoleLauncher --fail-fast is not a Maven flag. [JUnit release notes](https://docs.junit.org/6.1.0/release-notes.html)
- @FunctionalInterface on Arguments does not mean lambda implementations first became possible in JUnit 6. Teach Arguments.of and Named for readability. [JUnit 5 Arguments](https://docs.junit.org/5.13.4/api/org.junit.jupiter.params/org/junit/jupiter/params/provider/Arguments.html)
- Real GBM orders can wait outside operating hours; limit orders need a matching counterparty. The simulator's immediate-fill contract is intentionally smaller. [GBM order types](https://gbm.com/faqs/con-que-tipo-de-ordenes-existen-en-trading-usa/)
- Do not present CETES as a fractional US ETF. They are Mexican government debt with their own instrument mechanics. [Cetesdirecto technical note](https://www.cetesdirecto.com/tablas/recursos/cetes_notaTecnica.pdf)
- Remove the proposed Mexican wash-sale exercise. It imports a US rule, and even that rule covers acquisitions within 30 days before or after the sale, not only afterward. [IRS Publication 550](https://www.irs.gov/publications/p550)
- Do not implement generic automatic 10% SAT withholding for every profitable sale, or universal 10% dividend withholding. Product documentation distinguishes fiscal information and different dividend obligations. These topics require a separately scoped tax specification. [Fintual fiscal guide](https://ayuda.fintual.mx/es/articles/14011534-como-obtengo-la-guia-fiscal-para-mis-inversiones-en-fintual-acciones), [GBM dividend taxes](https://gbm.com/faqs/como-funcionan-los-impuestos-por-dividendos-en-trading-usa)
- Fintual documents FIFO for its realized-performance metric; that does not establish a universal Mexican statutory tax-lot policy. [Fintual realized gain](https://ayuda.fintual.mx/es/articles/10628519-como-se-calcula-la-ganancia-perdida-realizada)
