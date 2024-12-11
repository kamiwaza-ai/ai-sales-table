"use client"

import * as React from "react"
import { useEffect, useState } from "react"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import { api, type Column, type Row, WebSocketClient } from "@/lib/api"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"

export function DataGrid() {
  const [columns, setColumns] = useState<Column[]>([])
  const [rows, setRows] = useState<Row[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [website, setWebsite] = useState("")
  const [addingWebsite, setAddingWebsite] = useState(false)
  const [wsConnected, setWsConnected] = useState(false)

  const loadData = async () => {
    try {
      const data = await api.getData()
      const uniqueColumns = Array.from(
        new Map(data.columns.map((col: Column) => [col.name, col])).values()
      )
      setColumns(uniqueColumns)
      setRows(data.rows)
      setError(null)
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to load data")
    } finally {
      setLoading(false)
    }
  }

  const ws = React.useRef<WebSocketClient | null>(null);

  useEffect(() => {
    ws.current = new WebSocketClient((data: { type: string }) => {
      if (data.type === "update") {
        loadData();
      }
    });

    ws.current.connect();
    setWsConnected(true);

    return () => {
      ws.current?.disconnect();
    }
  }, []);

  const handleAddWebsite = async (e: React.FormEvent) => {
    e.preventDefault()
    setAddingWebsite(true)
    setError(null)

    try {
      if (website.trim()) {
        await api.addRow(website.trim())
        // Remove loadData() call since we'll get updates via WebSocket
        setWebsite("")
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to add website")
    } finally {
      setAddingWebsite(false)
    }
  }

  if (loading) {
    return <div className="p-8 text-center">Loading...</div>
  }

  if (error) {
    return (
      <div className="p-8 text-center">
        <p className="text-red-500 mb-4">{error}</p>
        <Button onClick={loadData}>Retry</Button>
      </div>
    )
  }

  return (
    <div className="space-y-6">
      <form onSubmit={handleAddWebsite} className="space-y-4">
        <div className="flex justify-between items-center">
          <div className="flex-1">
            <label htmlFor="website" className="block text-sm font-medium mb-2">
              Website URL
            </label>
            <div className="flex gap-2">
              <Input
                id="website"
                type="url"
                value={website}
                onChange={(e) => setWebsite(e.target.value)}
                placeholder="e.g., www.kamiwaza.ai"
                required
              />
              <Button type="submit" disabled={addingWebsite}>
                {addingWebsite ? "Adding..." : "Add Website"}
              </Button>
            </div>
          </div>
          <div className="flex gap-2">
            <Button
              type="button"
              onClick={() => api.refreshData()}
              disabled={columns.length === 0}
            >
              Refresh Data
            </Button>
            <Button
              type="button"
              variant="destructive"
              onClick={() => api.clearColumns()}
              disabled={columns.length === 0}
            >
              Clear All Columns
            </Button>
          </div>
        </div>
      </form>

      <div className="border rounded-lg">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Website</TableHead>
              {columns.map((column) => (
                <TableHead key={column.id}>{column.name}</TableHead>
              ))}
            </TableRow>
          </TableHeader>
          <TableBody>
            {rows.map((row) => (
              <TableRow key={row.id}>
                <TableCell>{row.website}</TableCell>
                {columns.map((column) => (
                  <TableCell key={`${row.id}-${column.id}`}>
                    {row.data[column.name] || ''}
                  </TableCell>
                ))}
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>
    </div>
  )
}
