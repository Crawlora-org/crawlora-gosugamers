import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class GosuGamersClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  article(params: OperationParamsMap["gosugamers-article"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  articles(params?: OperationParamsMap["gosugamers-articles"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  encounters(params: OperationParamsMap["gosugamers-encounters"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  games(params?: OperationParamsMap["gosugamers-games"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  match(params: OperationParamsMap["gosugamers-match"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchGame(params: OperationParamsMap["gosugamers-match-game"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matches(params?: OperationParamsMap["gosugamers-matches"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  player(params: OperationParamsMap["gosugamers-player"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  rankings(params: OperationParamsMap["gosugamers-rankings"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  results(params?: OperationParamsMap["gosugamers-results"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  stageGroups(params: OperationParamsMap["gosugamers-stage-groups"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  team(params: OperationParamsMap["gosugamers-team"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamResults(params: OperationParamsMap["gosugamers-team-results"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tournament(params: OperationParamsMap["gosugamers-tournament"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tournamentParticipants(params: OperationParamsMap["gosugamers-tournament-participants"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tournamentTalents(params: OperationParamsMap["gosugamers-tournament-talents"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tournaments(params?: OperationParamsMap["gosugamers-tournaments"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  article(params: OperationParamsMap["gosugamers-article"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  articles(params?: OperationParamsMap["gosugamers-articles"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  encounters(params: OperationParamsMap["gosugamers-encounters"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  games(params?: OperationParamsMap["gosugamers-games"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  match(params: OperationParamsMap["gosugamers-match"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchGame(params: OperationParamsMap["gosugamers-match-game"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matches(params?: OperationParamsMap["gosugamers-matches"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  player(params: OperationParamsMap["gosugamers-player"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  rankings(params: OperationParamsMap["gosugamers-rankings"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  results(params?: OperationParamsMap["gosugamers-results"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  stageGroups(params: OperationParamsMap["gosugamers-stage-groups"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  team(params: OperationParamsMap["gosugamers-team"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamResults(params: OperationParamsMap["gosugamers-team-results"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tournament(params: OperationParamsMap["gosugamers-tournament"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tournamentParticipants(params: OperationParamsMap["gosugamers-tournament-participants"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tournamentTalents(params: OperationParamsMap["gosugamers-tournament-talents"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tournaments(params?: OperationParamsMap["gosugamers-tournaments"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  article(...args: OperationRequestArgs<"gosugamers-article">): Promise<OperationResponseMap["gosugamers-article"]>;
  articles(...args: OperationRequestArgs<"gosugamers-articles">): Promise<OperationResponseMap["gosugamers-articles"]>;
  encounters(...args: OperationRequestArgs<"gosugamers-encounters">): Promise<OperationResponseMap["gosugamers-encounters"]>;
  games(...args: OperationRequestArgs<"gosugamers-games">): Promise<OperationResponseMap["gosugamers-games"]>;
  match(...args: OperationRequestArgs<"gosugamers-match">): Promise<OperationResponseMap["gosugamers-match"]>;
  matchGame(...args: OperationRequestArgs<"gosugamers-match-game">): Promise<OperationResponseMap["gosugamers-match-game"]>;
  matches(...args: OperationRequestArgs<"gosugamers-matches">): Promise<OperationResponseMap["gosugamers-matches"]>;
  player(...args: OperationRequestArgs<"gosugamers-player">): Promise<OperationResponseMap["gosugamers-player"]>;
  rankings(...args: OperationRequestArgs<"gosugamers-rankings">): Promise<OperationResponseMap["gosugamers-rankings"]>;
  results(...args: OperationRequestArgs<"gosugamers-results">): Promise<OperationResponseMap["gosugamers-results"]>;
  stageGroups(...args: OperationRequestArgs<"gosugamers-stage-groups">): Promise<OperationResponseMap["gosugamers-stage-groups"]>;
  team(...args: OperationRequestArgs<"gosugamers-team">): Promise<OperationResponseMap["gosugamers-team"]>;
  teamResults(...args: OperationRequestArgs<"gosugamers-team-results">): Promise<OperationResponseMap["gosugamers-team-results"]>;
  tournament(...args: OperationRequestArgs<"gosugamers-tournament">): Promise<OperationResponseMap["gosugamers-tournament"]>;
  tournamentParticipants(...args: OperationRequestArgs<"gosugamers-tournament-participants">): Promise<OperationResponseMap["gosugamers-tournament-participants"]>;
  tournamentTalents(...args: OperationRequestArgs<"gosugamers-tournament-talents">): Promise<OperationResponseMap["gosugamers-tournament-talents"]>;
  tournaments(...args: OperationRequestArgs<"gosugamers-tournaments">): Promise<OperationResponseMap["gosugamers-tournaments"]>;
}
export { GosuGamersClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default GosuGamersClient;
