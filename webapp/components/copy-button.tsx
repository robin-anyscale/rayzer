"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Check, Copy } from "lucide-react"

interface CopyButtonProps {
  text: string
  className?: string
}

export function CopyButton({ text, className }: CopyButtonProps) {
  const [isCopied, setIsCopied] = useState(false)

  const copy = async () => {
    await navigator.clipboard.writeText(text)
    setIsCopied(true)
    setTimeout(() => setIsCopied(false), 2000)
  }

  return (
    <Button
      size="sm"
      variant="ghost"
      className={`h-8 w-8 rounded-full bg-white shadow-sm border border-gray-200 ${className}`}
      onClick={copy}
    >
      {isCopied ? <Check className="h-4 w-4 text-green-500" /> : <Copy className="h-4 w-4 text-gray-700" />}
      <span className="sr-only">Copy command</span>
    </Button>
  )
}

