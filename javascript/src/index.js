import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class GosuGamersClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-gosugamers-js/0.1.0" });
    this["article"] = (...args) => this.request("gosugamers-article", ...args);
    this["articles"] = (...args) => this.request("gosugamers-articles", ...args);
    this["encounters"] = (...args) => this.request("gosugamers-encounters", ...args);
    this["games"] = (...args) => this.request("gosugamers-games", ...args);
    this["match"] = (...args) => this.request("gosugamers-match", ...args);
    this["matchGame"] = (...args) => this.request("gosugamers-match-game", ...args);
    this["matches"] = (...args) => this.request("gosugamers-matches", ...args);
    this["player"] = (...args) => this.request("gosugamers-player", ...args);
    this["rankings"] = (...args) => this.request("gosugamers-rankings", ...args);
    this["results"] = (...args) => this.request("gosugamers-results", ...args);
    this["stageGroups"] = (...args) => this.request("gosugamers-stage-groups", ...args);
    this["team"] = (...args) => this.request("gosugamers-team", ...args);
    this["teamResults"] = (...args) => this.request("gosugamers-team-results", ...args);
    this["tournament"] = (...args) => this.request("gosugamers-tournament", ...args);
    this["tournamentParticipants"] = (...args) => this.request("gosugamers-tournament-participants", ...args);
    this["tournamentTalents"] = (...args) => this.request("gosugamers-tournament-talents", ...args);
    this["tournaments"] = (...args) => this.request("gosugamers-tournaments", ...args);
  }
}

export { GosuGamersClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default GosuGamersClient;
