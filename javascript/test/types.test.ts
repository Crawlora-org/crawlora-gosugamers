import { GosuGamersClient } from "../src/index.js";

const client = new GosuGamersClient({ apiKey: "test-key" });
void client.article({"id": "sample"});
void client.request("gosugamers-article", {"id": "sample"});
const streamResponse: Promise<Response> = client.request("gosugamers-article", {"id": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("gosugamers-article", {"id": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.article({"id": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("gosugamers-article", {"id": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("gosugamers-article", {"id": "sample"}, { responseType: "text" });
void rawText;


void client.articles();
void client.request("gosugamers-articles");
// @ts-expect-error The selected operation requires its documented params.
void client.article();
