"use client"

import * as React from "react"
import { DataGrid } from "@/components/data-grid"
import { ColumnForm } from "@/components/column-form"

export default function Home() {
  return (
    <main className="container mx-auto py-8">
      <h1 className="mb-8 text-3xl font-bold">Sales Research Assistant</h1>

      <div className="mb-8">
        <h2 className="mb-4 text-xl font-semibold">Add New Column</h2>
        <ColumnForm />
      </div>

      <div>
        <h2 className="mb-4 text-xl font-semibold">Research Data</h2>
        <DataGrid />
      </div>
    </main>
  )
}
